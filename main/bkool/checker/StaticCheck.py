
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
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


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
        o[ast.classname.name] = {}
        [self.visit(x, o[ast.classname.name]) for x in ast.memlist]

    def visitMethodDecl(self, ast, o):
        # kind: SIKind
        # name: Id
        # param: List[VarDecl]
        # returnType: Type  # None for constructor
        # body: Block
        if ast.name.name in o:
            raise Redeclared(Method(), ast.name.name)
        o[ast.name.name] = {}

    def visitAttributeDecl(self, ast, o):
        # kind: SIKind #Instance or Static
        # decl: StoreDecl # VarDecl for mutable or ConstDecl for immutable
        if type(ast.decl) is VarDecl:
            if ast.decl.variable.name in o:
                raise Redeclared(Attribute(), ast.decl.variable.name)
            o[ast.decl.variable.name] = ast.decl.varType
        else:
            if ast.decl.constant.name in o:
                raise Redeclared(Attribute(), ast.decl.constant.name)
            o[ast.decl.constant.name] = ast.decl.constType

    def visitConstDecl(self, ast, o):
        # constant : Id
        # constType : Type
        # value : Expr
        if ast.constant.name in o:
            raise Redeclared(Constant(), ast.constant.name)
        o[ast.variable.name] = ast.constType

    def visitVarDecl(self, ast, o):
        # variable : Id
        # varType : Type
        # varInit : Expr = None # None if there is no initial
        if ast.variable.name in o:
            raise Redeclared(Variable(), ast.variable.name)
        o[ast.variable.name] = ast.varType


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
        env = GetEnv().visit(ast, None)
        return [self.visit(x, env) for x in ast.decl]

    def visitClassDecl(self, ast, o):
        env = {}
        env['current'] = ast.classname.name
        env['global'] = o
        for mem in ast.memlist:
            if type(mem) is MethodDecl:
                self.visit(mem, env)

    def visitMethodDecl(self, ast, o):
        # kind: SIKind
        # name: Id
        # param: List[VarDecl]
        # returnType: Type  # None for constructor
        # body: Block
        env = {}
        env['current'] = o['current']
        env['global'] = o['global']
        env['local'] = {}
        [GetEnv().visit(parameter, env['local']) for parameter in ast.param]
        self.visit(ast.body, env['local'])

    def visitBlock(self, ast, o):
        # decl:List[StoreDecl]
        # stmt:List[Stmt]
        [GetEnv().visit(decl, o) for decl in ast.decl]

    def visitBinaryOp(self, ast, o):
        # op:str
        # left:Expr
        # right:Expr
        l = self.visit(ast.left, o)
        r = self.visit(ast.right, o)
        print(o)
        #Arithmetic
        if ast.op in ['+', '-', '*', '/', '\\', '%']:
            print('Alo')

    def visitId(self, ast, o):
        if ast.name in o:
            return o[ast.name]
        raise Undeclared(Identifier(), ast.name)

    def visitIntLiteral(self, ast, o):
        return 'Int'

    def visitFloatLiteral(self, ast, o):
        return 'Float'

    def visitBooleanLiteral(self, ast, o):
        return 'Boolean'

    def visitStringLiteral(self, ast, o):
        return 'String'

    def visitNullLiteral(self, ast, o):
        return 'Null'

    # def visitSelfLiteral(self, ast, param):
