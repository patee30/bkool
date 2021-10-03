grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}
program: classDecl+ EOF;

//------------------------CLASS----------------------------------

classDecl: CLASS ID (EXTENDS parentID)? classBody;
parentID: ID;

classBody: LC classBodyList? RC;

classBodyList: classMem | classMem classBodyList;

classMem: attributeDecl | methodDecl;
//------------------------ATTRIBUTE-----------------------------
attributeDecl:
	STATIC? FINAL? mtype varDecl_list SM
	| FINAL? STATIC? mtype varDecl_list SM;

varDecl_init: ID (EQUAL exp)?;
varDecl_list: varDecl_init | varDecl_init COMMA varDecl_list;
//-------------------------METHOD-----------------------------
methodDecl: STATIC? mtype? ID LB param? RB block_stmt;
param: methodParameter | methodParameter SM param;
methodParameter: mtype parameterList;
parameterList: ID | ID COMMA parameterList;

varDecl: FINAL? mtype varDecl_list SM;

//------------------------EXPRESSION------------------------
exp: exp1 (LT | LE | GT | GE) exp1 | exp1;

exp1: exp2 (IS_EQUAL | NOT_EQUAL) exp2 | exp2;

exp2: exp2 (AND | OR) exp3 | exp3;

exp3: exp3 (PLUS | SUB) exp4 | exp4;

exp4: exp4 (MUL | DIV | FLOAT_DIV | MOD) exp5 | exp5;

exp5: exp5 CONCATE exp6 | exp6;

exp6: NOT exp6 | exp7;

exp7: (PLUS | SUB) exp7 | exp8;

exp8: (exp9 LS exp RS) | exp9;

exp9:
	exp9 DOT ID (LB expList RB)
	| exp9 DOT ID (LB RB)
	| exp9 DOT ID
	| exp10;

exp10: NEW ID LB expList RB | NEW ID LB RB | exp11;

exp11: LB exp RB | operand;

operand: literal | ID;

mtype:
	mtype LS INTLIT RS
	| INTTYPE
	| FLOATTYPE
	| STRINGTYPE
	| BOOLTYPE
	| ID
	| VOID_TYPE;

//------------------------STATEMENTS---------------------------

stmt:
	block_stmt
	| if_stmt
	| assign_stmt
	| for_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| call_stmt;

stmtList: stmt | stmt stmtList;

block_stmt:
	LC varDeclList stmtList RC
	| LC varDeclList RC
	| LC stmtList RC
	| LC RC;

varDeclList: varDecl | varDecl varDeclList;
assign_stmt: lhs ASSIGN exp SM;
lhs: ID | exp9 DOT ID | exp9 LS exp RS;

if_stmt: IF exp THEN stmt (ELSE stmt)?;

for_stmt: FOR for_condition (TO | DOWN_TO) exp DO stmt;

for_condition: ID ASSIGN exp;

break_stmt: BREAK SM;
continue_stmt: CONTINUE SM;

return_stmt: RETURN exp SM;

call_stmt: exp9 DOT ID LB expList? RB SM;

expList: exp | exp COMMA expList;
//-------------------------TYPE--------------------------------

INTTYPE: 'int';
FLOATTYPE: 'float';
VOID_TYPE: 'void';
BOOLTYPE: 'boolean';
STRINGTYPE: 'string';

//------------------------KEYWORDS-------------------------------
CLASS: 'class';
EXTENDS: 'extends';
STATIC: 'static';
FINAL: 'final';
BREAK: 'break';
CONTINUE: 'continue';
DO: 'do';
ELSE: 'else';
IF: 'if';
THEN: 'then';
FOR: 'for';
RETURN: 'return';
TRUE: 'true';
FALSE: 'false';
NIL: 'nil';
THIS: 'this';
TO: 'to';
DOWN_TO: 'downto';

//---------------------FRAGMENTS-----------------------------------
fragment Digit: [0-9];
fragment NonDigit: [a-zA-Z_];
fragment LowerCase: [a-z];
fragment UpperCase: [A-Z];
fragment ExponentPart: [eE] [-+]? Digit+;
fragment DecimalPart: '.' Digit*;

fragment STR_CHAR: STR_ESCAPE_LEG | STR_CHAR_LEG;
fragment STR_CHAR_LEG: ~["\n\\];
fragment STR_ESCAPE_LEG: '\\' [bfrnt"\\];
fragment ILLEGAL_STRING: '\\' ~[bfrnt"\\];
//-----------------LITERALS---------------------
arraylit: LC literalList RC;

literalList: literal | literal COMMA literalList;
literal:
	INTLIT
	| FLOATLIT
	| boollit
	| STRINGLIT
	| arraylit
	| THIS
	| NIL;

boollit: TRUE | FALSE;

INTLIT: Digit+;

FLOATLIT:
	Digit+ (
		DecimalPart? ExponentPart
		| DecimalPart ExponentPart?
	);

BOOLLIT: TRUE | FALSE;

STRINGLIT:
	'"' STR_CHAR*? '"' {
	self.text=str(self.text)
};

//---------------SEPARATOR-------------------
LB: '(';
RB: ')';

LC: '{';
RC: '}';

LS: '[';
RS: ']';

COLON: ':';
DOT: '.';
COMMA: ',';
SM: ';';

//----------------OPERATOR-----------------
EQUAL: '=';
ASSIGN: ':=';
PLUS: '+';
MUL: '*';
DIV: '\\';
NOT_EQUAL: '!=';
LT: '<';
LE: '<=';
OR: '||';
NOT: '!';
NEW: 'new';
SUB: '-';
FLOAT_DIV: '/';
MOD: '%';
IS_EQUAL: '==';
GT: '>';
GE: '>=';
AND: '&&';
CONCATE: '^';

//-----------------ID--------------------
ID: NonDigit (NonDigit | Digit)*;

//----------------------COMMENTS------------------------
COMMENT_1: '/*' .*? '*/' -> skip;
COMMENT_2: '#' .*? ([\n] | EOF) -> skip;

WS: [ \t\r\n\f]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR:
	.{
    raise ErrorToken(self.text)
};
UNCLOSE_STRING:
	'"' STR_CHAR* {
    raise UncloseString(self.text)
};
ILLEGAL_ESCAPE:
	'"' STR_CHAR*? ILLEGAL_STRING {
        raise IllegalEscape(self.text)
    };
