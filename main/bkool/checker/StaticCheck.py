
"""
 * @author nhphung
"""
#from AST import *
#from Visitor import *
from Utils import Utils
from StaticError import *
from main.bkool.utils.AST import *
from main.bkool.utils.Visitor import BaseVisitor


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None, details=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.details = details


class Env:
    def __init__(self, globalEnv={}, localEnv=None, currentEnv=None):
        self.o = {}
        self.o['global'] = globalEnv
        self.o['local'] = localEnv
        self.o['current'] = currentEnv

    def openScope(self, o):
        o['local'].append({})

    def closeScope(self, o):
        o['local'].pop()

    def lookUp(self, name):
        if len(self.o['local']):
            if name in self.o['local'][-1]:
                return True
            return False
        else:
            pass


class Sup:
    def lookUp(self):
        pass

    def lookUpLocal(self):
        pass


class GetEnv(BaseVisitor):
    def visit(self, ast, param):
        return ast.accept(self, param)

    def visitProgram(self, ast, o):
        # decl : List[ClassDecl]
        o = {}
        [self.visit(x, o) for x in ast.decl]
        return o

    def visitClassDecl(self, ast, o):
        # classname : Id
        # memlist : List[MemDecl]
        # parentname : Id = None # None if there is no parent
        if ast.classname.name in o:
            raise Redeclared(Class(), ast.classname.name)
        o[ast.classname.name] = {
            'parent': ast.parentname.name if ast.parentname else None,
            'members': {}
        }
        [self.visit(x, o[ast.classname.name]['members']) for x in ast.memlist]

    def visitMethodDecl(self, ast, o):
        # kind: SIKind
        # name: Id
        # param: List[VarDecl]
        # returnType: Type  # None for constructor
        # body: Block
        if ast.name.name in o:
            raise Redeclared(Method(), ast.name.name)
        o[ast.name.name] = [ast.kind, Symbol(ast.name.name, ast.returnType), None]

    def visitAttributeDecl(self, ast, o):
        # kind: SIKind #Instance or Static
        # decl: StoreDecl # VarDecl for mutable or ConstDecl for immutable
        decl = ast.decl
        value = None
        if type(decl) is VarDecl:
            if decl.variable.name in o:
                raise Redeclared(Attribute(), decl.variable.name)
            if type(decl.varType) is ClassType:
                # if not decl.varType.classname.name in o['global']:
                #     raise Undeclared(Class(), decl.varType.classname.name)
                value = 'objClass'
            o[decl.variable.name] = [ast.kind, Symbol(decl.variable.name, decl.varType, value)]
        else:
            if decl.constant.name in o:
                raise Redeclared(Attribute(), decl.constant.name)
            value = 'constant'
            # if type(decl.constType) is ClassType:
            #     if not decl.constType.classname.name in o['global']:
            #         raise Undeclared(Class(), decl.constType.classname.name)
            o[decl.constant.name] = [ast.kind, Symbol(decl.constant.name, decl.constType, value)]

class StaticChecker(BaseVisitor):

    def visit(self, ast, param):
        return ast.accept(self, param)

    global_envi = [
        Symbol("readInt", MType([], IntType())),
        Symbol("writeInt", MType([IntType()], VoidType())),
        Symbol("writeIntLn", MType([IntType()], VoidType())),
        Symbol("readFloat", MType([FloatType()], FloatType())),
        Symbol("writeFloat", MType([FloatType()], VoidType())),
        Symbol("writeFloatLn", MType([FloatType()], VoidType())),
        Symbol("readBool", MType([BoolType()], BoolType())),
        Symbol("writeBool", MType([BoolType()], VoidType())),
        Symbol("writeBoolLn", MType([BoolType()], VoidType())),
        Symbol("readStr", MType([], StringType())),
        Symbol("writeStr", MType([StringType()], VoidType())),
        Symbol("writeStrLn", MType([StringType()], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, o):
        env = GetEnv().visit(ast, Env())
        return [self.visit(x, env) for x in ast.decl]

    def visitClassDecl(self, ast, o):
        env = {}
        env['global'] = o
        env['current'] = ast.classname.name
        for mem in ast.memlist:
            self.visit(mem, env)

    def visitMethodDecl(self, ast, o):
        # kind: SIKind
        # name: Id
        # param: List[VarDecl]
        # returnType: Type  # None for constructor
        # body: Block
        env = {}
        env['global'] = o['global']
        env['current'] = o['current']
        env['local'] = {}
        [self.visit(parameter, env) for parameter in ast.param]
        self.visit(ast.body, env)

    def visitAttributeDecl(self, ast, o):
        # kind: SIKind #Instance or Static
        # decl: StoreDecl # VarDecl for mutable or ConstDecl for immutable
        decl = ast.decl
        if type(decl) is VarDecl:
            if type(decl.varType) is ClassType:
                if not decl.varType.classname.name in o['global']:
                    raise Undeclared(Class(), decl.varType.classname.name)
        if type(decl) is ConstDecl:
            if type(decl.constType) is ClassType:
                if not decl.constType.classname.name in o['global']:
                    raise Undeclared(Class(), decl.constType.classname.name)
            value_typ = self.visit(decl.value, o).mtype
            if type(decl.constType) is IntType:
                if type(value_typ) != IntType: raise TypeMismatchInConstant(decl)
            elif type(decl.constType) is FloatType:
                if not type(value_typ) in [IntType, FloatType]: raise TypeMismatchInConstant(decl)
            elif type(decl.constType) is BoolType:
                if type(value_typ) != BoolType: raise TypeMismatchInConstant(decl)
            # o['global'][o['current']]['members'][ast.decl.constant.name] = [ast.kind, Symbol(decl.constant.name, typ, 'constant')]

    def visitConstDecl(self, ast, o):
        # constant : Id
        # constType : Type
        # value : Expr
        if ast.constant.name in o['local']:
            raise Redeclared(Constant(), ast.constant.name)
        elif ast.constant.name in o['global'][o['current']]['members']:
            raise Redeclared(Constant(), ast.constant.name)
        if type(ast.constType) is ClassType:
            if not ast.constType.classname.name in o['global']:
                raise Undeclared(Class(), ast.constType.classname.name)
        elif type(ast.constType) is IntType:
            if type(self.visit(ast.value, o).mtype) != IntType:
                raise TypeMismatchInConstant(ast)
        elif type(ast.constType) is FloatType:
            if not self.visit(ast.value, o).mtype in [IntType, FloatType]:
                raise TypeMismatchInConstant(ast)
        elif type(ast.constDecl) is BoolType:
            if self.visit(ast.value, o).mtype != BoolType:
                raise TypeMismatchInConstant(ast)
        o['local'][ast.constant.name] = Symbol(ast.constant.name, ast.constType, 'constant')

    def visitVarDecl(self, ast, o):
        # variable : Id
        # varType : Type
        # varInit : Expr = None # None if there is no initial
        if ast.variable.name in o['local']:
            raise Redeclared(Variable(), ast.variable.name)
        if type(ast.varType) is ClassType:
            if not ast.varType.classname.name in o['global']:
                raise Undeclared(Class(), ast.varType.classname.name)
        o['local'][ast.variable.name] = Symbol(ast.variable.name, ast.varType)

    def visitBlock(self, ast, o):
        # decl:List[StoreDecl]
        # stmt:List[Stmt]
        [self.visit(decl, o) for decl in ast.decl]
        [self.visit(stmt, o) for stmt in ast.stmt]

    def visitBinaryOp(self, ast, o):
        # op:str
        # left:Expr
        # right:Expr
        l = self.visit(ast.left, o)
        r = self.visit(ast.right, o)
        if l is None:
            raise Undeclared(Identifier(), ast.left.name)
        if r is None:
            raise Undeclared(Identifier(), ast.right.name)
        # Arithmetic
        if ast.op in ['+', '-', '*', '/', '\\', '%']:
            if not l.mtype and r.mtype in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            elif type(l.mtype) != type(r.mtype) and l.mtype != IntType and (ast.op in ['\\', '%']):
                raise TypeMismatchInExpression(ast)
            elif ast.op == '/':
                return Symbol('', FloatType)
            elif type(l.mtype) != type(r.mtype):
                return Symbol('', FloatType)
            else:
                return l

        # Boolean
        elif ast.op in ['&&', '||']:
            if not l.mtype and r.mtype == BoolType:
                raise TypeMismatchInExpression(ast)
            else:
                return Symbol('', BoolType)

        # Relational
        elif ast.op in ['==', '!=', '>', '<', '>=', '<=']:
            if ast.op in ['==', '!=']:
                if (not l.mtype and r.mtype in [IntType, BoolType]) or type(l.mtype) != type(r.mtype):
                    raise TypeMismatchInExpression(ast)
            else:
                if (not l.mtype and r.mtype in [IntType, FloatType]):
                    raise TypeMismatchInExpression(ast)

            return Symbol('', BoolType)

        # String
        elif ast.op == '^':
            if l.mtype and r.mtype != StringType:
                raise TypeMismatchInExpression(ast)
            return Symbol('', BoolType)

    def visitUnaryOp(self, ast, o):
        # op:str
        # body:Expr
        body = self.visit(ast.body, o)

        if ast.op in ['+', '-']:
            if not body.mtype in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            else:
                return body.mtype

        elif ast.op == '!':
            if body.mtype != BoolType:
                raise TypeMismatchInExpression(ast)

    def visitAssign(self, ast, o):
        # lhs:Expr
        # exp:Expr
        lhs = self.visit(ast.lhs, o)
        if lhs.value == 'constant': raise CannotAssignToConstant(ast)

        exp = self.visit(ast.exp, o)
        if type(lhs.mtype) != type(exp.mtype):
            raise TypeMismatchInStatement(ast)

    def visitFieldAccess(self, ast, o):
        # obj:Expr
        # fieldname:Id
        obj = self.visit(ast.obj, o)
        typ = 'objClass'
        obj_name = obj.mtype.classname if type(obj.mtype) == ClassType else obj.name
        if type(obj.mtype) != ClassType:
            raise TypeMismatchInExpression(ast)
        
   
        if obj.value in ['objClass', 'class']:
            ancestor = obj_name.name if type(obj_name) == Id else obj_name
            while ancestor != None:
                if ast.fieldname.name in o['global'][ancestor]['members']:                
                    if obj.value == 'class':
                        if o['global'][ancestor]['members'][ast.fieldname.name][0] == Instance():
                            raise IllegalMemberAccess(ast)
                    elif obj.value == 'objClass':
                        if o['global'][ancestor]['members'][ast.fieldname.name][0] == Static():
                            raise IllegalMemberAccess(ast)
                    typ = o['global'][ancestor]['members'][ast.fieldname.name][1]
                    return Symbol('', typ)
                else: ancestor = o['global'][ancestor]['parent']

            raise Undeclared(Identifier(), ast.fieldname.name)
        else:
            raise Undeclared(Class(), obj.name)
        
        
    def visitId(self, ast, o):
        value = None
        name = ast.name
        if ast.name in o['local']:
            if type(o['local'][ast.name].mtype) == ClassType:  
                value = 'objClass'
                name = o['local'][ast.name].mtype.classname.name
            if o['local'][ast.name].value == 'constant':
                value = 'constant'
            return Symbol(name, o['local'][ast.name].mtype, value)

        if ast.name in o['global'][o['current']]['members']:
            if o['global'][o['current']]['members'][ast.name][1].value == 'constant':
                return  o['global'][o['current']]['members'][ast.name][1]
            else:
                return Symbol(o['current'], o['global'][o['current']]['members'][ast.name][1], 'memClass')
 
        if ast.name in o['global']:
            return Symbol(ast.name, ClassType(ast.name), 'class')

        raise Undeclared(Identifier(), ast.name)

    def visitIntLiteral(self, ast, o):
        return Symbol('', IntType())

    def visitFloatLiteral(self, ast, o):
        return Symbol('', FloatType())

    def visitBooleanLiteral(self, ast, o):
        return Symbol('', BoolType())

    def visitStringLiteral(self, ast, o):
        return Symbol('', StringType())

    def visitNullLiteral(self, ast, o):
        pass

    def visitSelfLiteral(self, ast, o):
        return Symbol(o['current'], ClassType( o['current']), 'objClass')
