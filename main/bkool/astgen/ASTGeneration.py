from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from main.bkool.utils.AST import *
from functools import reduce


class ASTGeneration(BKOOLVisitor):
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        class_decls = list(
            reduce(
                lambda y, x: y + [self.visit(x)],
                [item for item in ctx.classDecl()],
                [],
            )
        )
        return Program(class_decls)

    def visitClassDecl(self, ctx: BKOOLParser.ClassDeclContext):
        class_name = Id(ctx.ID().getText())
        parent_name = self.visit(ctx.parentID()) if ctx.parentID() else None
        mem_list = self.visit(ctx.classBody())
        return ClassDecl(class_name, mem_list, parent_name)

    def visitParentID(self, ctx: BKOOLParser.ParentIDContext):
        return Id(ctx.ID().getText())

    def visitClassBody(self, ctx: BKOOLParser.ClassBodyContext):
        return self.visit(ctx.classBodyList()) if ctx.classBodyList() else []

    def visitClassBodyList(self, ctx: BKOOLParser.ClassBodyListContext):
        return self.visit(ctx.classMem()) + (
            self.visit(ctx.classBodyList()) if ctx.classBodyList() else []
        )

    def visitClassMem(self, ctx: BKOOLParser.ClassMemContext):
        return (
            self.visit(ctx.attributeDecl())
            if ctx.attributeDecl()
            else [self.visit(ctx.methodDecl())]
        )

    def visitAttributeDecl(self, ctx: BKOOLParser.AttributeDeclContext):
        kind = Static() if ctx.STATIC() else Instance()
        type = self.visit(ctx.mtype())
        var_list = self.visit(ctx.varDecl_list())

        return (
            list(
                map(
                    lambda x: AttributeDecl(kind, ConstDecl(x[0], type, x[1])), var_list
                )
            )
            if ctx.FINAL()
            else list(
                map(lambda x: AttributeDecl(kind, VarDecl(x[0], type, x[1])), var_list)
            )
        )

    def visitVarDecl_list(self, ctx: BKOOLParser.VarDecl_listContext):
        return [self.visit(ctx.varDecl_init())] + (
            self.visit(ctx.varDecl_list()) if ctx.varDecl_list() else []
        )

    def visitVarDecl_init(self, ctx: BKOOLParser.VarDecl_initContext):
        return (Id(ctx.ID().getText()), self.visit(ctx.exp()) if ctx.exp() else None)

    def visitVarDecl(self, ctx: BKOOLParser.VarDeclContext):
        varType = self.visit(ctx.mtype())
        return [VarDecl(x, varType, y) for (x, y) in self.visit(ctx.varDecl_list())]

    def visitMethodDecl(self, ctx: BKOOLParser.MethodDeclContext):
        kind = Static() if ctx.STATIC() else Instance()
        name = Id(ctx.ID().getText()) if ctx.mtype() else Id("<init>")
        param = self.visit(ctx.param()) if ctx.param() else []
        type = self.visit(ctx.mtype()) if ctx.mtype() else None
        body = self.visit(ctx.block_stmt())
        return MethodDecl(kind, name, param, type, body)

    def visitParam(self, ctx: BKOOLParser.ParamContext):
        return self.visit(ctx.methodParameter()) + (
            self.visit(ctx.param()) if ctx.param() else []
        )

    def visitMethodParameter(self, ctx: BKOOLParser.MethodParameterContext):
        param_list = self.visit(ctx.parameterList())
        type = self.visit(ctx.mtype())
        return list(map(lambda x: VarDecl(x, type), param_list))

    def visitParameterList(self, ctx: BKOOLParser.ParameterListContext):
        return [Id(ctx.ID().getText())] + (
            self.visit(ctx.parameterList()) if ctx.parameterList() else []
        )

    def visitBlock_stmt(self, ctx: BKOOLParser.Block_stmtContext):
        return Block(
            self.visit(ctx.varDeclList()) if ctx.varDeclList() else [],
            self.visit(ctx.stmtList()) if ctx.stmtList() else [],
        )

    def visitVarDeclList(self, ctx: BKOOLParser.VarDeclListContext):
        return self.visit(ctx.varDecl()) + (
            self.visit(ctx.varDeclList()) if ctx.varDeclList() else []
        )

    def visitVarDecl(self, ctx: BKOOLParser.VarDeclContext):
        type = self.visit(ctx.mtype())
        var_list = self.visit(ctx.varDecl_list())
        return (
            list(map(lambda x: ConstDecl(x[0], type, x[1]), var_list))
            if ctx.FINAL()
            else list(map(lambda x: VarDecl(x[0], type, x[1]), var_list))
        )

    def visitStmtList(self, ctx: BKOOLParser.StmtListContext):
        return [self.visit(ctx.stmt())] + (
            self.visit(ctx.stmtList()) if ctx.stmtList() else []
        )

    def visitStmt(self, ctx: BKOOLParser.StmtContext):
        return self.visit(ctx.getChild(0))

    def visitIf_stmt(self, ctx: BKOOLParser.If_stmtContext):
        expr = self.visit(ctx.exp())
        thenStmt = self.visit(ctx.stmt(0))
        elseStmt = self.visit(ctx.stmt(1)) if ctx.ELSE() else None
        return If(expr, thenStmt, elseStmt)

    def visitAssign_stmt(self, ctx: BKOOLParser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.exp())
        return Assign(lhs, exp)

    def visitLhs(self, ctx: BKOOLParser.LhsContext):
        if ctx.exp():
            return ArrayCell(self.visit(ctx.exp9()), self.visit(ctx.exp()))
        elif ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        else:
            return FieldAccess(self.visit(ctx.exp9()), Id(ctx.ID().getText()))

    def visitFor_stmt(self, ctx: BKOOLParser.For_stmtContext):
        (id, expr1) = self.visit(ctx.for_condition())
        expr2 = self.visit(ctx.exp())
        up = True if ctx.TO() else False
        loop = self.visit(ctx.stmt())
        return For(id, expr1, expr2, up, loop)

    def visitFor_condition(self, ctx: BKOOLParser.For_conditionContext):
        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.exp())
        return (id, expr1)

    def visitBreak_stmt(self, ctx: BKOOLParser.Break_stmtContext):
        return Break()

    def visitContinue_stmt(self, ctx: BKOOLParser.Continue_stmtContext):
        return Continue()

    def visitReturn_stmt(self, ctx: BKOOLParser.Return_stmtContext):
        return Return(self.visit(ctx.exp()))

    def visitCall_stmt(self, ctx: BKOOLParser.Call_stmtContext):
        return CallStmt(
            self.visit(ctx.exp9()),
            Id(ctx.ID().getText()),
            self.visit(ctx.expList()) if ctx.expList() else [],
        )

    def visitExpList(self, ctx: BKOOLParser.ExpListContext):
        return [self.visit(ctx.exp())] + (
            self.visit(ctx.expList()) if ctx.expList() else []
        )

    def visitExp(self, ctx: BKOOLParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            return BinaryOp(op, left, right)

    def visitExp1(self, ctx: BKOOLParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.exp2(0))
            right = self.visit(ctx.exp2(1))
            return BinaryOp(op, left, right)

    def visitExp2(self, ctx: BKOOLParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            return BinaryOp(op, left, right)

    def visitExp3(self, ctx: BKOOLParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            return BinaryOp(op, left, right)

    def visitExp4(self, ctx: BKOOLParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.exp4())
            right = self.visit(ctx.exp5())
            return BinaryOp(op, left, right)

    def visitExp5(self, ctx: BKOOLParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        else:
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.exp5())
            right = self.visit(ctx.exp6())
            return BinaryOp(op, left, right)

    def visitExp6(self, ctx: BKOOLParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        else:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.exp6())
            return UnaryOp(op, body)

    def visitExp7(self, ctx: BKOOLParser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp8())
        else:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.exp7())
            return UnaryOp(op, body)

    def visitExp8(self, ctx: BKOOLParser.Exp8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp9())
        else:
            arr = self.visit(ctx.exp9())
            idx = self.visit(ctx.exp())
            return ArrayCell(arr, idx)

    def visitExp9(self, ctx: BKOOLParser.Exp9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp10())
        elif ctx.getChildCount() == 3:
            obj = self.visit(ctx.exp9())
            fieldname = Id(ctx.ID().getText())
            return FieldAccess(obj, fieldname)
        else:
            obj = self.visit(ctx.exp9())
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.expList()) if ctx.expList() else []
            return CallExpr(obj, method, param)

    def visitExp10(self, ctx: BKOOLParser.Exp10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp11())
        else:
            classname = Id(ctx.ID().getText())
            param = self.visit(ctx.expList()) if ctx.expList() else []
            return NewExpr(classname, param)

    def visitExp11(self, ctx: BKOOLParser.Exp11Context):
        return self.visit(ctx.exp()) if ctx.exp() else self.visit(ctx.operand())

    def visitOperand(self, ctx: BKOOLParser.OperandContext):
        return Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.literal())

    def visitLiteral(self, ctx: BKOOLParser.LiteralContext):
        return (
            IntLiteral(int(ctx.INTLIT().getText()))
            if ctx.INTLIT()
            else FloatLiteral(float(ctx.FLOATLIT().getText()))
            if ctx.FLOATLIT()
            else self.visit(ctx.boollit())
            if ctx.boollit()
            else StringLiteral(ctx.STRINGLIT().getText())
            if ctx.STRINGLIT()
            else self.visit(ctx.arraylit())
            if ctx.arraylit()
            else SelfLiteral()
            if ctx.THIS()
            else NullLiteral()
        )

    def visitBoollit(self, ctx: BKOOLParser.BoollitContext):
        return BooleanLiteral(True if ctx.TRUE() else False)

    def visitArraylit(self, ctx: BKOOLParser.ArraylitContext):
        return ArrayLiteral(self.visit(ctx.literalList()))

    def visitLiteralList(self, ctx: BKOOLParser.LiteralListContext):
        return [self.visit(ctx.literal())] + (
            self.visit(ctx.literalList()) if ctx.literalList() else []
        )

    def visitMtype(self, ctx: BKOOLParser.MtypeContext):
        if ctx.getChildCount() == 1:
            if ctx.INTTYPE():
                return IntType()
            elif ctx.FLOATTYPE():
                return FloatType()
            elif ctx.STRINGTYPE():
                return StringType()
            elif ctx.BOOLTYPE():
                return BoolType()
            elif ctx.ID():
                return ClassType(Id(ctx.ID().getText()))
            elif ctx.VOID_TYPE():
                return VoidType()
        else:
            return ArrayType(int(ctx.INTLIT().getText()), self.visit(ctx.mtype()))
