import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    """1. DECLARATION"""

    def test_simple_class_decl_1(self):
        """single class"""
        input = """
            class Spec0 {
            }
        """
        expect = str(Program([ClassDecl(Id("Spec0"), [])]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_simple_class_decl_2(self):
        """multiple classes"""
        input = """
            class Spec1 {
            }
            class Spec2 {
            }
            class Spec3 {
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(Id("Spec1"), []),
                    ClassDecl(Id("Spec2"), []),
                    ClassDecl(Id("Spec3"), []),
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_class_decl_3(self):
        """single derived class"""
        input = """
            class InputStream extends Stream {
            }
        """
        expect = str(Program([ClassDecl(Id("InputStream"), [], Id("Stream"))]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_simple_class_decl_4(self):
        """multiple derived classes"""
        input = """
            class SingleLinkedList extends LL {
            }
            class DoubleLinkedList extends LL {
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(Id("SingleLinkedList"), [], Id("LL")),
                    ClassDecl(Id("DoubleLinkedList"), [], Id("LL")),
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_advance_class_decl_1(self):
        """multiple classes"""
        input = """
            class Sort {
            }
            class QuickSort extends Sort {
            }
            class MergeSort extends Sort {
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(Id("Sort"), []),
                    ClassDecl(Id("QuickSort"), [], Id("Sort")),
                    ClassDecl(Id("MergeSort"), [], Id("Sort")),
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_simple_attribute_decl_1(self):
        """single instance attribute in single statement"""
        input = """
            class Exam {
                int score;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Exam"),
                        [AttributeDecl(Instance(), VarDecl(Id("score"), IntType()))],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_simple_attribute_decl_2(self):
        """multiple instance attributes in single statement"""
        input = """
            class Gravity {
                float res, v = 10e+4, g = 9.800, h = 0100., s = 5.e7;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Gravity"),
                        [
                            AttributeDecl(Instance(), VarDecl(Id("res"), FloatType())),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("v"), FloatType(), FloatLiteral(100000.0)),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("g"), FloatType(), FloatLiteral(9.8)),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("h"), FloatType(), FloatLiteral(100.0)),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("s"), FloatType(), FloatLiteral(50000000.0)),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_simple_attribute_decl_3(self):
        """multiple instance attributes in multiple statements"""
        input = """
            class Triangle {
                bool isScalene = false, isIsosceles;
                bool isEquilateral;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Triangle"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("isScalene"),
                                    ClassType(Id("bool")),
                                    BooleanLiteral(False),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("isIsosceles"), ClassType(Id("bool"))),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("isEquilateral"), ClassType(Id("bool"))),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_simple_attribute_decl_4(self):
        """multiple instance attributes in multiple statements"""
        input = """
            class Someone {
                string firstName = \"Nguyen\", middleName = \"null\", lastName;
                string email = \"example@mail.com\";
                string address = \"001/01 Ly Thuong Kiet, Dict 10, Viet Nam\";
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Someone"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("firstName"),
                                    StringType(),
                                    StringLiteral('"Nguyen"'),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("middleName"),
                                    StringType(),
                                    StringLiteral('"null"'),
                                ),
                            ),
                            AttributeDecl(
                                Instance(), VarDecl(Id("lastName"), StringType())
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("email"),
                                    StringType(),
                                    StringLiteral('"example@mail.com"'),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("address"),
                                    StringType(),
                                    StringLiteral(
                                        '"001/01 Ly Thuong Kiet, Dict 10, Viet Nam"'
                                    ),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_simple_attribute_decl_5(self):
        """multiple instance attributes in multiple statements"""
        input = """
            class Matrix {
                int[1234] m1, m2;
                float[567][890][123][40] random = {true, 6, 2.e4};
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Matrix"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("m1"), ArrayType(1234, IntType())),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("m2"), ArrayType(1234, IntType())),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("random"),
                                    ArrayType(
                                        40,
                                        ArrayType(
                                            123,
                                            ArrayType(890, ArrayType(567, FloatType())),
                                        ),
                                    ),
                                    ArrayLiteral(
                                        [
                                            BooleanLiteral(True),
                                            IntLiteral(6),
                                            FloatLiteral(20000.0),
                                        ]
                                    ),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_simple_attribute_decl_6(self):
        """multiple instance attributes in multiple statements"""
        input = """
            class Subject {
                static int id, major;
                StudentId[100] students = {5e-912, \"sth\"};
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Subject"),
                        [
                            AttributeDecl(Static(), VarDecl(Id("id"), IntType())),
                            AttributeDecl(Static(), VarDecl(Id("major"), IntType())),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("students"),
                                    ArrayType(100, ClassType(Id("StudentId"))),
                                    ArrayLiteral(
                                        [FloatLiteral(0.0), StringLiteral('"sth"')]
                                    ),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_simple_attribute_decl_7(self):
        """multiple instance attributes in multiple statements"""
        input = """
            class DrawLayer {
                Point a = new Point(3, 5), b = new Point(1, 43.7), c = new Point(999, 01);
                Triangle trg = new Triangle(a, b, c);
                Paint paint = new Paint();
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("DrawLayer"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("a"),
                                    ClassType(Id("Point")),
                                    NewExpr(
                                        Id("Point"), [IntLiteral(3), IntLiteral(5)]
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("b"),
                                    ClassType(Id("Point")),
                                    NewExpr(
                                        Id("Point"), [IntLiteral(1), FloatLiteral(43.7)]
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("c"),
                                    ClassType(Id("Point")),
                                    NewExpr(
                                        Id("Point"), [IntLiteral(999), IntLiteral(1)]
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("trg"),
                                    ClassType(Id("Triangle")),
                                    NewExpr(
                                        Id("Triangle"), [Id("a"), Id("b"), Id("c")]
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("paint"),
                                    ClassType(Id("Paint")),
                                    NewExpr(Id("Paint"), []),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_simple_attribute_decl_8(self):
        """multiple instance attributes in multiple statements"""
        input = """
            class VoidType {
                void x = 1;
                void[4] y = {\"sth\"};
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("VoidType"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("x"), VoidType(), IntLiteral(1))
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("y"),
                                    ArrayType(4, VoidType()),
                                    ArrayLiteral([StringLiteral('"sth"')]),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_simple_attribute_decl_9(self):
        """multiple const attributes in single statement"""
        input = """
            class Heap {
                final HeapElement[100] maxheap = {\"a\", \"b\"}, minHeap;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Heap"),
                        [
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("maxheap"),
                                    ArrayType(100, ClassType(Id("HeapElement"))),
                                    ArrayLiteral(
                                        [StringLiteral('"a"'), StringLiteral('"b"')]
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("minHeap"),
                                    ArrayType(100, ClassType(Id("HeapElement"))),
                                    None,
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_simple_attribute_decl_10(self):
        """multiple static attributes in single statement"""
        input = """
            class ConstNumber {
                static float num = 234.e-6309, num2, num3;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("ConstNumber"),
                        [
                            AttributeDecl(
                                Static(),
                                VarDecl(Id("num"), FloatType(), FloatLiteral(0.0)),
                            ),
                            AttributeDecl(Static(), VarDecl(Id("num2"), FloatType())),
                            AttributeDecl(Static(), VarDecl(Id("num3"), FloatType())),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_simple_attribute_decl_11(self):
        """multiple attributes in multiple statements"""
        input = """
            class Recursion {
                static string val = \"not init\";
                final int lvl = 1, numOfRecursion;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Recursion"),
                        [
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("val"), StringType(), StringLiteral('"not init"')
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(Id("lvl"), IntType(), IntLiteral(1)),
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(Id("numOfRecursion"), IntType(), None),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_simple_attribute_decl_12(self):
        """multiple attributes in multiple statements"""
        input = """
            class AttrDecl {
                static final int age = 1;
                final static string name = \"John\";
                static final bool gender = true;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("AttrDecl"),
                        [
                            AttributeDecl(
                                Static(), ConstDecl(Id("age"), IntType(), IntLiteral(1))
                            ),
                            AttributeDecl(
                                Static(),
                                ConstDecl(
                                    Id("name"), StringType(), StringLiteral('"John"')
                                ),
                            ),
                            AttributeDecl(
                                Static(),
                                ConstDecl(
                                    Id("gender"),
                                    ClassType(Id("bool")),
                                    BooleanLiteral(True),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_advanced_attribute_decl_1(self):
        """mixed attributes"""
        input = """
            class AttrDeclAdvanced {
                int size = 100, idx;
                final float pivot = 6e-81;
                static bool flag1, flag2 = true;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("AttrDeclAdvanced"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(Id("size"), IntType(), IntLiteral(100)),
                            ),
                            AttributeDecl(Instance(), VarDecl(Id("idx"), IntType())),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("pivot"), FloatType(), FloatLiteral(6e-81)
                                ),
                            ),
                            AttributeDecl(
                                Static(), VarDecl(Id("flag1"), ClassType(Id("bool")))
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("flag2"),
                                    ClassType(Id("bool")),
                                    BooleanLiteral(True),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_advanced_attribute_decl_2(self):
        """mixed attributes"""
        input = """
            class AttrDeclAdvanced {
                final static string[400] name, address;
                void[400][400] comment;
                static final Class[400] obj = new Class();
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("AttrDeclAdvanced"),
                        [
                            AttributeDecl(
                                Static(),
                                ConstDecl(
                                    Id("name"), ArrayType(400, StringType()), None
                                ),
                            ),
                            AttributeDecl(
                                Static(),
                                ConstDecl(
                                    Id("address"), ArrayType(400, StringType()), None
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("comment"),
                                    ArrayType(400, ArrayType(400, VoidType())),
                                ),
                            ),
                            AttributeDecl(
                                Static(),
                                ConstDecl(
                                    Id("obj"),
                                    ArrayType(400, ClassType(Id("Class"))),
                                    NewExpr(Id("Class"), []),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_simple_parameter_decl_1(self):
        """multiple parameters"""
        input = """
            class Module {
                Void nothing() {}
                int main (int argc; char[100] argv) {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Module"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("nothing"),
                                [],
                                ClassType(Id("Void")),
                                Block([], []),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [
                                    VarDecl(Id("argc"), IntType()),
                                    VarDecl(
                                        Id("argv"),
                                        ArrayType(100, ClassType(Id("char"))),
                                    ),
                                ],
                                IntType(),
                                Block([], []),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_advanced_parameter_decl_1(self):
        """multiple parameters"""
        input = """
            class ExternalSort {
                init (List[100] list1, list2; int size1, size2) {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("ExternalSort"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("<init>"),
                                [
                                    VarDecl(
                                        Id("list1"),
                                        ArrayType(100, ClassType(Id("List"))),
                                    ),
                                    VarDecl(
                                        Id("list2"),
                                        ArrayType(100, ClassType(Id("List"))),
                                    ),
                                    VarDecl(Id("size1"), IntType()),
                                    VarDecl(Id("size2"), IntType()),
                                ],
                                None,
                                Block([], []),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_simple_function_decl_1(self):
        """single instance constructor"""
        input = """
            class SimpleInit {
                init() {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("SimpleInit"),
                        [MethodDecl(Instance(), Id("<init>"), [], None, Block([], []))],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_simple_function_decl_2(self):
        """single instance constructor"""
        input = """
            class BubbleSort {
                constructor(int[1000] arr; bool earlyTerminate) {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("BubbleSort"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("<init>"),
                                [
                                    VarDecl(Id("arr"), ArrayType(1000, IntType())),
                                    VarDecl(
                                        Id("earlyTerminate"), ClassType(Id("bool"))
                                    ),
                                ],
                                None,
                                Block([], []),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_simple_function_decl_3(self):
        """multiple instance constructors"""
        input = """
            class Job {
                init (User user_info; Company _compinfo) {}
                constructor() {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Job"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("<init>"),
                                [
                                    VarDecl(Id("user_info"), ClassType(Id("User"))),
                                    VarDecl(Id("_compinfo"), ClassType(Id("Company"))),
                                ],
                                None,
                                Block([], []),
                            ),
                            MethodDecl(
                                Instance(), Id("<init>"), [], None, Block([], [])
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_simple_function_decl_4(self):
        """single static constructor"""
        input = """
            class Job {
                static init() {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Job"),
                        [MethodDecl(Static(), Id("<init>"), [], None, Block([], []))],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_simple_function_decl_5(self):
        """multiple constructors"""
        input = """
            class Job {
                init() {}
                static init(int param1, param2) {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Job"),
                        [
                            MethodDecl(
                                Instance(), Id("<init>"), [], None, Block([], [])
                            ),
                            MethodDecl(
                                Static(),
                                Id("<init>"),
                                [
                                    VarDecl(Id("param1"), IntType()),
                                    VarDecl(Id("param2"), IntType()),
                                ],
                                None,
                                Block([], []),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_simple_function_decl_6(self):
        """single instance function"""
        input = """
            class Func {
                string hello() {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Func"),
                        [
                            MethodDecl(
                                Instance(), Id("hello"), [], StringType(), Block([], [])
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_simple_function_decl_7(self):
        """multiple instance functions"""
        input = """
            class String {
                int len() {}
                string [100] split(string delimiter) {}
                something strip() {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("String"),
                        [
                            MethodDecl(
                                Instance(), Id("len"), [], IntType(), Block([], [])
                            ),
                            MethodDecl(
                                Instance(),
                                Id("split"),
                                [VarDecl(Id("delimiter"), StringType())],
                                ArrayType(100, StringType()),
                                Block([], []),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("strip"),
                                [],
                                ClassType(Id("something")),
                                Block([], []),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_simple_function_decl_8(self):
        """multiple static functions"""
        input = """
            class String {
                static int len() {}
                static string [100] split(string delimiter) {}
                static something strip() {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("String"),
                        [
                            MethodDecl(
                                Static(), Id("len"), [], IntType(), Block([], [])
                            ),
                            MethodDecl(
                                Static(),
                                Id("split"),
                                [VarDecl(Id("delimiter"), StringType())],
                                ArrayType(100, StringType()),
                                Block([], []),
                            ),
                            MethodDecl(
                                Static(),
                                Id("strip"),
                                [],
                                ClassType(Id("something")),
                                Block([], []),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_advanced_function_decl_1(self):
        """mixed functions"""
        input = """
            class a {
                void [9] b(float c, d; int e) {}
                Class f(Class g, h, i) {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("a"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("b"),
                                [
                                    VarDecl(Id("c"), FloatType()),
                                    VarDecl(Id("d"), FloatType()),
                                    VarDecl(Id("e"), IntType()),
                                ],
                                ArrayType(9, VoidType()),
                                Block([], []),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("f"),
                                [
                                    VarDecl(Id("g"), ClassType(Id("Class"))),
                                    VarDecl(Id("h"), ClassType(Id("Class"))),
                                    VarDecl(Id("i"), ClassType(Id("Class"))),
                                ],
                                ClassType(Id("Class")),
                                Block([], []),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_advanced_function_decl_2(self):
        """mixed functions"""
        input = """
            class Sticker {
                static Note writeNote (string[100] list) {}
                bool deleteNote(int idx) {}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Sticker"),
                        [
                            MethodDecl(
                                Static(),
                                Id("writeNote"),
                                [VarDecl(Id("list"), ArrayType(100, StringType()))],
                                ClassType(Id("Note")),
                                Block([], []),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("deleteNote"),
                                [VarDecl(Id("idx"), IntType())],
                                ClassType(Id("bool")),
                                Block([], []),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_simple_variable_decl_1(self):
        """single variable in single statement"""
        input = """
            class Hello {
                void hello() {
                    string msg = \"Hello world!\\n\";
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Hello"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("hello"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("msg"),
                                            StringType(),
                                            StringLiteral('"Hello world!\\n"'),
                                        )
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_simple_variable_decl_2(self):
        """multilpe variables in single statement"""
        input = """
            class TestServer {
                static string uri;
                bool getRequest(string payload) {
                    string method = \"GET\", content_length = String.len(payload), response;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("TestServer"),
                        [
                            AttributeDecl(Static(), VarDecl(Id("uri"), StringType())),
                            MethodDecl(
                                Instance(),
                                Id("getRequest"),
                                [VarDecl(Id("payload"), StringType())],
                                ClassType(Id("bool")),
                                Block(
                                    [
                                        VarDecl(
                                            Id("method"),
                                            StringType(),
                                            StringLiteral('"GET"'),
                                        ),
                                        VarDecl(
                                            Id("content_length"),
                                            StringType(),
                                            CallExpr(
                                                Id("String"), Id("len"), [Id("payload")]
                                            ),
                                        ),
                                        VarDecl(Id("response"), StringType()),
                                    ],
                                    [],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_simple_variable_decl_3(self):
        """multilpe variables in multiple statements"""
        input = """
            class Car {
                static string mode(int idx) {
                    int maxIdx = 3, minIdx = 0, flag;
                    string [3] mode = {\"Stop\", \"Slow\", \"Normal\", \"Fast\"};
                    float vel = 0.e+0, fuel = 0100.;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Car"),
                        [
                            MethodDecl(
                                Static(),
                                Id("mode"),
                                [VarDecl(Id("idx"), IntType())],
                                StringType(),
                                Block(
                                    [
                                        VarDecl(Id("maxIdx"), IntType(), IntLiteral(3)),
                                        VarDecl(Id("minIdx"), IntType(), IntLiteral(0)),
                                        VarDecl(Id("flag"), IntType()),
                                        VarDecl(
                                            Id("mode"),
                                            ArrayType(3, StringType()),
                                            ArrayLiteral(
                                                [
                                                    StringLiteral('"Stop"'),
                                                    StringLiteral('"Slow"'),
                                                    StringLiteral('"Normal"'),
                                                    StringLiteral('"Fast"'),
                                                ]
                                            ),
                                        ),
                                        VarDecl(
                                            Id("vel"), FloatType(), FloatLiteral(0.0)
                                        ),
                                        VarDecl(
                                            Id("fuel"), FloatType(), FloatLiteral(100.0)
                                        ),
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_simple_variable_decl_4(self):
        """single const variable in single statement"""
        input = """
            class ConstString {
                string get() {
                    final string val = 2021;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("ConstString"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("get"),
                                [],
                                StringType(),
                                Block(
                                    [
                                        ConstDecl(
                                            Id("val"), StringType(), IntLiteral(2021)
                                        )
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_simple_variable_decl_5(self):
        """multiple const variable in multiple statements"""
        input = """
            class ConstClass {
                int get() {
                    final int g;
                    final float pi = 3.1415926536, e = \"2.7182818284\";
                    final bool sqrt2 = 001.41421, sqrt3 = new False(), sqrt4;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("ConstClass"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("get"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        ConstDecl(Id("g"), IntType(), None),
                                        ConstDecl(
                                            Id("pi"),
                                            FloatType(),
                                            FloatLiteral(3.1415926536),
                                        ),
                                        ConstDecl(
                                            Id("e"),
                                            FloatType(),
                                            StringLiteral('"2.7182818284"'),
                                        ),
                                        ConstDecl(
                                            Id("sqrt2"),
                                            ClassType(Id("bool")),
                                            FloatLiteral(1.41421),
                                        ),
                                        ConstDecl(
                                            Id("sqrt3"),
                                            ClassType(Id("bool")),
                                            NewExpr(Id("False"), []),
                                        ),
                                        ConstDecl(
                                            Id("sqrt4"), ClassType(Id("bool")), None
                                        ),
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_advanced_variable_decl_1(self):
        """mixed variables"""
        input = """
            class MixedVar {
                float getVal() {
                    int num1 = 99, num2;
                    final float char1 = 08e-8, char2 = True;
                    string char3 = False, num3 = x;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("MixedVar"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("getVal"),
                                [],
                                FloatType(),
                                Block(
                                    [
                                        VarDecl(Id("num1"), IntType(), IntLiteral(99)),
                                        VarDecl(Id("num2"), IntType()),
                                        ConstDecl(
                                            Id("char1"),
                                            FloatType(),
                                            FloatLiteral(8e-08),
                                        ),
                                        ConstDecl(Id("char2"), FloatType(), Id("True")),
                                        VarDecl(Id("char3"), StringType(), Id("False")),
                                        VarDecl(Id("num3"), StringType(), Id("x")),
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_advanced_variable_decl_2(self):
        """mixed variables"""
        input = """
            class Files {
                bool setPrivileges(int usercode) {
                    bool user, group, admin;
                    final FileTable tbl = new Table(usercode);
                    int[200] _idx_lst, file_lst;
                    final File[100] userfile = {\"mybk\", \"drive\"};
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Files"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("setPrivileges"),
                                [VarDecl(Id("usercode"), IntType())],
                                ClassType(Id("bool")),
                                Block(
                                    [
                                        VarDecl(Id("user"), ClassType(Id("bool"))),
                                        VarDecl(Id("group"), ClassType(Id("bool"))),
                                        VarDecl(Id("admin"), ClassType(Id("bool"))),
                                        ConstDecl(
                                            Id("tbl"),
                                            ClassType(Id("FileTable")),
                                            NewExpr(Id("Table"), [Id("usercode")]),
                                        ),
                                        VarDecl(
                                            Id("_idx_lst"), ArrayType(200, IntType())
                                        ),
                                        VarDecl(
                                            Id("file_lst"), ArrayType(200, IntType())
                                        ),
                                        ConstDecl(
                                            Id("userfile"),
                                            ArrayType(100, ClassType(Id("File"))),
                                            ArrayLiteral(
                                                [
                                                    StringLiteral('"mybk"'),
                                                    StringLiteral('"drive"'),
                                                ]
                                            ),
                                        ),
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_all_decl_1(self):
        """mixed declarations"""
        input = """
            class MemLoc {
                static final MemBlock[10100] block_list = nil;
                init(int id) {
                    final void name = \"block\\\"0x00\", pointer;
                    bool status, written = true;
                    Header[10] meta = new Pointer(id);
                }
                static getContent(Pointer p; bool canread, canwrite) {
                    void var;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("MemLoc"),
                        [
                            AttributeDecl(
                                Static(),
                                ConstDecl(
                                    Id("block_list"),
                                    ArrayType(10100, ClassType(Id("MemBlock"))),
                                    NullLiteral(),
                                ),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("<init>"),
                                [VarDecl(Id("id"), IntType())],
                                None,
                                Block(
                                    [
                                        ConstDecl(
                                            Id("name"),
                                            VoidType(),
                                            StringLiteral('"block\\"0x00"'),
                                        ),
                                        ConstDecl(Id("pointer"), VoidType(), None),
                                        VarDecl(Id("status"), ClassType(Id("bool"))),
                                        VarDecl(
                                            Id("written"),
                                            ClassType(Id("bool")),
                                            BooleanLiteral(True),
                                        ),
                                        VarDecl(
                                            Id("meta"),
                                            ArrayType(10, ClassType(Id("Header"))),
                                            NewExpr(Id("Pointer"), [Id("id")]),
                                        ),
                                    ],
                                    [],
                                ),
                            ),
                            MethodDecl(
                                Static(),
                                Id("<init>"),
                                [
                                    VarDecl(Id("p"), ClassType(Id("Pointer"))),
                                    VarDecl(Id("canread"), ClassType(Id("bool"))),
                                    VarDecl(Id("canwrite"), ClassType(Id("bool"))),
                                ],
                                None,
                                Block([VarDecl(Id("var"), VoidType())], []),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_all_decl_2(self):
        """mixed declarations"""
        input = """
            class Base {
                final static string [1][2][3] text, tmp = false;
                bool [9] func1() {}
                C1 func3 (int param1, param2; bool param3; float param4; string[9] param5) {}
            }
            
            class Derive1 extends Base {
                concreteFunc1() {}
                concreteFunc2() {}
            }
            
            class Derive2 extends Derive1 {
                void attr1, attr2 = None;
            }
            
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Base"),
                        [
                            AttributeDecl(
                                Static(),
                                ConstDecl(
                                    Id("text"),
                                    ArrayType(
                                        3, ArrayType(2, ArrayType(1, StringType()))
                                    ),
                                    None,
                                ),
                            ),
                            AttributeDecl(
                                Static(),
                                ConstDecl(
                                    Id("tmp"),
                                    ArrayType(
                                        3, ArrayType(2, ArrayType(1, StringType()))
                                    ),
                                    BooleanLiteral(False),
                                ),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("func1"),
                                [],
                                ArrayType(9, ClassType(Id("bool"))),
                                Block([], []),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("func3"),
                                [
                                    VarDecl(Id("param1"), IntType()),
                                    VarDecl(Id("param2"), IntType()),
                                    VarDecl(Id("param3"), ClassType(Id("bool"))),
                                    VarDecl(Id("param4"), FloatType()),
                                    VarDecl(Id("param5"), ArrayType(9, StringType())),
                                ],
                                ClassType(Id("C1")),
                                Block([], []),
                            ),
                        ],
                    ),
                    ClassDecl(
                        Id("Derive1"),
                        [
                            MethodDecl(
                                Instance(), Id("<init>"), [], None, Block([], [])
                            ),
                            MethodDecl(
                                Instance(), Id("<init>"), [], None, Block([], [])
                            ),
                        ],
                        Id("Base"),
                    ),
                    ClassDecl(
                        Id("Derive2"),
                        [
                            AttributeDecl(Instance(), VarDecl(Id("attr1"), VoidType())),
                            AttributeDecl(
                                Instance(), VarDecl(Id("attr2"), VoidType(), Id("None"))
                            ),
                        ],
                        Id("Derive1"),
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 340))

    """2. EXPRESSION"""

    def test_relational_exp_1(self):
        """comparison: <, >, <=, >="""
        input = """
            class Rel {
                static bool a = 1 > 2, b = \"something\" < false;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Rel"),
                        [
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("a"),
                                    ClassType(Id("bool")),
                                    BinaryOp(">", IntLiteral(1), IntLiteral(2)),
                                ),
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("b"),
                                    ClassType(Id("bool")),
                                    BinaryOp(
                                        "<",
                                        StringLiteral('"something"'),
                                        BooleanLiteral(False),
                                    ),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_relational_exp_2(self):
        """comparison: <, >, <=, >="""
        input = """
            class Rel {
                int main() {
                    final string c = 523e09 <= 83923;
                    if d >= 9 then
                        return \"sdfg\" < {this};
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Rel"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        ConstDecl(
                                            Id("c"),
                                            StringType(),
                                            BinaryOp(
                                                "<=",
                                                FloatLiteral(523000000000.0),
                                                IntLiteral(83923),
                                            ),
                                        )
                                    ],
                                    [
                                        If(
                                            BinaryOp(">=", Id("d"), IntLiteral(9)),
                                            Return(
                                                BinaryOp(
                                                    "<",
                                                    StringLiteral('"sdfg"'),
                                                    ArrayLiteral([SelfLiteral()]),
                                                )
                                            ),
                                        )
                                    ],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_relational_exp_3(self):
        """comparison: ==, !="""
        input = """
            class Rel {
                final sth temp = false == false;
                bool temp2 = \"1\" != this;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Rel"),
                        [
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("temp"),
                                    ClassType(Id("sth")),
                                    BinaryOp(
                                        "==",
                                        BooleanLiteral(False),
                                        BooleanLiteral(False),
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("temp2"),
                                    ClassType(Id("bool")),
                                    BinaryOp("!=", StringLiteral('"1"'), SelfLiteral()),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_relational_exp_4(self):
        """comparison: ==, !="""
        input = """
            class Rel {
                int call(bool f) {
                    for t := 1 to 100 do return 2 == 1;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Rel"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [VarDecl(Id("f"), ClassType(Id("bool")))],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        For(
                                            Id("t"),
                                            IntLiteral(1),
                                            IntLiteral(100),
                                            True,
                                            Return(
                                                BinaryOp(
                                                    "==", IntLiteral(2), IntLiteral(1)
                                                )
                                            ),
                                        )
                                    ],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_boolean_exp_1(self):
        """bool: &&, ||"""
        input = """
            class Bool {
                string temp = 1 && 2, temp2 = true || 6e7;
                static bool x = \"18\" && False && true || b.d();
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Bool"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("temp"),
                                    StringType(),
                                    BinaryOp("&&", IntLiteral(1), IntLiteral(2)),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("temp2"),
                                    StringType(),
                                    BinaryOp(
                                        "||",
                                        BooleanLiteral(True),
                                        FloatLiteral(60000000.0),
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("x"),
                                    ClassType(Id("bool")),
                                    BinaryOp(
                                        "||",
                                        BinaryOp(
                                            "&&",
                                            BinaryOp(
                                                "&&", StringLiteral('"18"'), Id("False")
                                            ),
                                            BooleanLiteral(True),
                                        ),
                                        CallExpr(Id("b"), Id("d"), []),
                                    ),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_boolean_exp_2(self):
        """bool: &&, ||"""
        input = """
            class Bool {
                int call() {
                    final def a = 0.e+5 || {\"a\"} || false && \"something\";
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Bool"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        ConstDecl(
                                            Id("a"),
                                            ClassType(Id("def")),
                                            BinaryOp(
                                                "&&",
                                                BinaryOp(
                                                    "||",
                                                    BinaryOp(
                                                        "||",
                                                        FloatLiteral(0.0),
                                                        ArrayLiteral(
                                                            [StringLiteral('"a"')]
                                                        ),
                                                    ),
                                                    BooleanLiteral(False),
                                                ),
                                                StringLiteral('"something"'),
                                            ),
                                        )
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_arithmetic_exp_1(self):
        """integer/float: +, -"""
        input = """
            class Arith {
                opq add = 1 + 1, sub = {0192, {88}} - \"bruh\";
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Arith"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("add"),
                                    ClassType(Id("opq")),
                                    BinaryOp("+", IntLiteral(1), IntLiteral(1)),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("sub"),
                                    ClassType(Id("opq")),
                                    BinaryOp(
                                        "-",
                                        ArrayLiteral(
                                            [
                                                IntLiteral(192),
                                                ArrayLiteral([IntLiteral(88)]),
                                            ]
                                        ),
                                        StringLiteral('"bruh"'),
                                    ),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_arithmetic_exp_2(self):
        """integer/float: +, -"""
        input = """
            class Arith {
                int call() {
                    float res = 7242 + 1283 + 8123 + 31273 - 6239;
                    string res2 = 6e88 + \"sad\" - this - 18 - false;
                    nit res = 3 - 5e-12 - 1733 + \"hehe\" - 12;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Arith"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("res"),
                                            FloatType(),
                                            BinaryOp(
                                                "-",
                                                BinaryOp(
                                                    "+",
                                                    BinaryOp(
                                                        "+",
                                                        BinaryOp(
                                                            "+",
                                                            IntLiteral(7242),
                                                            IntLiteral(1283),
                                                        ),
                                                        IntLiteral(8123),
                                                    ),
                                                    IntLiteral(31273),
                                                ),
                                                IntLiteral(6239),
                                            ),
                                        ),
                                        VarDecl(
                                            Id("res2"),
                                            StringType(),
                                            BinaryOp(
                                                "-",
                                                BinaryOp(
                                                    "-",
                                                    BinaryOp(
                                                        "-",
                                                        BinaryOp(
                                                            "+",
                                                            FloatLiteral(6e88),
                                                            StringLiteral('"sad"'),
                                                        ),
                                                        SelfLiteral(),
                                                    ),
                                                    IntLiteral(18),
                                                ),
                                                BooleanLiteral(False),
                                            ),
                                        ),
                                        VarDecl(
                                            Id("res"),
                                            ClassType(Id("nit")),
                                            BinaryOp(
                                                "-",
                                                BinaryOp(
                                                    "+",
                                                    BinaryOp(
                                                        "-",
                                                        BinaryOp(
                                                            "-",
                                                            IntLiteral(3),
                                                            FloatLiteral(5e-12),
                                                        ),
                                                        IntLiteral(1733),
                                                    ),
                                                    StringLiteral('"hehe"'),
                                                ),
                                                IntLiteral(12),
                                            ),
                                        ),
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_arithmetic_exp_3(self):
        """integer/float: *, \, /, %"""
        input = """
            class Arith {
                int[2] e = f * g, f = true \\ a.b.c.d, mod = 7 % False;
                float acc = 9330 * \"hehe\", acc2 = d.e.f[1] / acc2;
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Arith"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("e"),
                                    ArrayType(2, IntType()),
                                    BinaryOp("*", Id("f"), Id("g")),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("f"),
                                    ArrayType(2, IntType()),
                                    BinaryOp(
                                        "\\",
                                        BooleanLiteral(True),
                                        FieldAccess(
                                            FieldAccess(
                                                FieldAccess(Id("a"), Id("b")), Id("c")
                                            ),
                                            Id("d"),
                                        ),
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("mod"),
                                    ArrayType(2, IntType()),
                                    BinaryOp("%", IntLiteral(7), Id("False")),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("acc"),
                                    FloatType(),
                                    BinaryOp(
                                        "*", IntLiteral(9330), StringLiteral('"hehe"')
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("acc2"),
                                    FloatType(),
                                    BinaryOp(
                                        "/",
                                        ArrayCell(
                                            FieldAccess(
                                                FieldAccess(Id("d"), Id("e")), Id("f")
                                            ),
                                            IntLiteral(1),
                                        ),
                                        Id("acc2"),
                                    ),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_arithmetic_exp_4(self):
        """integer/float: *, \, /, %"""
        input = """
            class Arith {
                int call() {
                    hehe[10][10] tmp = 1 * 2e3 * 3 * 4;
                    final string tmp2 = \"1\" / \"2\" / 3e5 / 4;
                    bool[10] tmp3 = o.p.q \\ false \\ \"True\" \\ {99};
                    float tmp4 = 1001010 % 8123 % \"haha\" % nil;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Arith"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("tmp"),
                                            ArrayType(
                                                10, ArrayType(10, ClassType(Id("hehe")))
                                            ),
                                            BinaryOp(
                                                "*",
                                                BinaryOp(
                                                    "*",
                                                    BinaryOp(
                                                        "*",
                                                        IntLiteral(1),
                                                        FloatLiteral(2000.0),
                                                    ),
                                                    IntLiteral(3),
                                                ),
                                                IntLiteral(4),
                                            ),
                                        ),
                                        ConstDecl(
                                            Id("tmp2"),
                                            StringType(),
                                            BinaryOp(
                                                "/",
                                                BinaryOp(
                                                    "/",
                                                    BinaryOp(
                                                        "/",
                                                        StringLiteral('"1"'),
                                                        StringLiteral('"2"'),
                                                    ),
                                                    FloatLiteral(300000.0),
                                                ),
                                                IntLiteral(4),
                                            ),
                                        ),
                                        VarDecl(
                                            Id("tmp3"),
                                            ArrayType(10, ClassType(Id("bool"))),
                                            BinaryOp(
                                                "\\",
                                                BinaryOp(
                                                    "\\",
                                                    BinaryOp(
                                                        "\\",
                                                        FieldAccess(
                                                            FieldAccess(
                                                                Id("o"), Id("p")
                                                            ),
                                                            Id("q"),
                                                        ),
                                                        BooleanLiteral(False),
                                                    ),
                                                    StringLiteral('"True"'),
                                                ),
                                                ArrayLiteral([IntLiteral(99)]),
                                            ),
                                        ),
                                        VarDecl(
                                            Id("tmp4"),
                                            FloatType(),
                                            BinaryOp(
                                                "%",
                                                BinaryOp(
                                                    "%",
                                                    BinaryOp(
                                                        "%",
                                                        IntLiteral(1001010),
                                                        IntLiteral(8123),
                                                    ),
                                                    StringLiteral('"haha"'),
                                                ),
                                                NullLiteral(),
                                            ),
                                        ),
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_arithmetic_exp_5(self):
        """integer/float: *, \, /, %"""
        input = """
            class Arith {
                int call() {
                    int random = 1e4 * \"haha\" % hehe / 123e-456 \\ false;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Arith"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("random"),
                                            IntType(),
                                            BinaryOp(
                                                "\\",
                                                BinaryOp(
                                                    "/",
                                                    BinaryOp(
                                                        "%",
                                                        BinaryOp(
                                                            "*",
                                                            FloatLiteral(10000.0),
                                                            StringLiteral('"haha"'),
                                                        ),
                                                        Id("hehe"),
                                                    ),
                                                    FloatLiteral(0.0),
                                                ),
                                                BooleanLiteral(False),
                                            ),
                                        )
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_arithmetic_exp_6(self):
        """integer/float: *, \, /, %"""
        input = """
            class Arith {
                int call() {
                    nill[100] a = \"haha\" % fasle % 12346 % 7123e-3 / 1237 / asd \\ \"g\" \\ 812 \\ \"array\" * 233 * true;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Arith"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("a"),
                                            ArrayType(100, ClassType(Id("nill"))),
                                            BinaryOp(
                                                "*",
                                                BinaryOp(
                                                    "*",
                                                    BinaryOp(
                                                        "\\",
                                                        BinaryOp(
                                                            "\\",
                                                            BinaryOp(
                                                                "\\",
                                                                BinaryOp(
                                                                    "/",
                                                                    BinaryOp(
                                                                        "/",
                                                                        BinaryOp(
                                                                            "%",
                                                                            BinaryOp(
                                                                                "%",
                                                                                BinaryOp(
                                                                                    "%",
                                                                                    StringLiteral(
                                                                                        '"haha"'
                                                                                    ),
                                                                                    Id(
                                                                                        "fasle"
                                                                                    ),
                                                                                ),
                                                                                IntLiteral(
                                                                                    12346
                                                                                ),
                                                                            ),
                                                                            FloatLiteral(
                                                                                7.123
                                                                            ),
                                                                        ),
                                                                        IntLiteral(
                                                                            1237
                                                                        ),
                                                                    ),
                                                                    Id("asd"),
                                                                ),
                                                                StringLiteral('"g"'),
                                                            ),
                                                            IntLiteral(812),
                                                        ),
                                                        StringLiteral('"array"'),
                                                    ),
                                                    IntLiteral(233),
                                                ),
                                                BooleanLiteral(True),
                                            ),
                                        )
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_string_exp_1(self):
        """concatenation: ^"""
        input = """
            class String {
                string temp = \"hello\" ^ \"world\";
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("String"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("temp"),
                                    StringType(),
                                    BinaryOp(
                                        "^",
                                        StringLiteral('"hello"'),
                                        StringLiteral('"world"'),
                                    ),
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_string_exp_2(self):
        """concatenation: ^"""
        input = """
            class String {
                int call() {
                    String request = \"Can I\" ^ \"fall\" ^ \"in\" ^ love ^ \"again?\", response = Yes ^ \"! ^_^\\\"\";
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("String"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("request"),
                                            ClassType(Id("String")),
                                            BinaryOp(
                                                "^",
                                                BinaryOp(
                                                    "^",
                                                    BinaryOp(
                                                        "^",
                                                        BinaryOp(
                                                            "^",
                                                            StringLiteral('"Can I"'),
                                                            StringLiteral('"fall"'),
                                                        ),
                                                        StringLiteral('"in"'),
                                                    ),
                                                    Id("love"),
                                                ),
                                                StringLiteral('"again?"'),
                                            ),
                                        ),
                                        VarDecl(
                                            Id("response"),
                                            ClassType(Id("String")),
                                            BinaryOp(
                                                "^",
                                                Id("Yes"),
                                                StringLiteral('"! ^_^\\""'),
                                            ),
                                        ),
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_boolean_exp_3(self):
        """bool: ! (unary)"""
        input = """
            class Bool {
                final bool a = !True, b = !false;
                int call() {
                    int c = !!1, d = !!!\"string\";
                    float e = !!!(!!!!(!false)), f = !!a.b().c();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Bool"),
                        [
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("a"),
                                    ClassType(Id("bool")),
                                    UnaryOp("!", Id("True")),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                ConstDecl(
                                    Id("b"),
                                    ClassType(Id("bool")),
                                    UnaryOp("!", BooleanLiteral(False)),
                                ),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("c"),
                                            IntType(),
                                            UnaryOp("!", UnaryOp("!", IntLiteral(1))),
                                        ),
                                        VarDecl(
                                            Id("d"),
                                            IntType(),
                                            UnaryOp(
                                                "!",
                                                UnaryOp(
                                                    "!",
                                                    UnaryOp(
                                                        "!", StringLiteral('"string"')
                                                    ),
                                                ),
                                            ),
                                        ),
                                        VarDecl(
                                            Id("e"),
                                            FloatType(),
                                            UnaryOp(
                                                "!",
                                                UnaryOp(
                                                    "!",
                                                    UnaryOp(
                                                        "!",
                                                        UnaryOp(
                                                            "!",
                                                            UnaryOp(
                                                                "!",
                                                                UnaryOp(
                                                                    "!",
                                                                    UnaryOp(
                                                                        "!",
                                                                        UnaryOp(
                                                                            "!",
                                                                            BooleanLiteral(
                                                                                False
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        VarDecl(
                                            Id("f"),
                                            FloatType(),
                                            UnaryOp(
                                                "!",
                                                UnaryOp(
                                                    "!",
                                                    CallExpr(
                                                        CallExpr(Id("a"), Id("b"), []),
                                                        Id("c"),
                                                        [],
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                    [],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_arithmetic_exp_7(self):
        """integer/float: +, - (unary)"""
        input = """
            class Arith {
                string temp = +1, temp2 = -\"false\", tmppp = +a.b.d, tmparray = -a[10];
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Arith"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("temp"),
                                    StringType(),
                                    UnaryOp("+", IntLiteral(1)),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("temp2"),
                                    StringType(),
                                    UnaryOp("-", StringLiteral('"false"')),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("tmppp"),
                                    StringType(),
                                    UnaryOp(
                                        "+",
                                        FieldAccess(
                                            FieldAccess(Id("a"), Id("b")), Id("d")
                                        ),
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("tmparray"),
                                    StringType(),
                                    UnaryOp("-", ArrayCell(Id("a"), IntLiteral(10))),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_arithmatic_exp_8(self):
        """integer/float: +, - (unary)"""
        input = """
            class Arithm {
                int call() {
                    chaos[9999] sth = ++++--\"1\", sth2 = --++++---hehe;
                    float sth3 = ---+(-+-+g.h().ij[12])[34];
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Arithm"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("sth"),
                                            ArrayType(9999, ClassType(Id("chaos"))),
                                            UnaryOp(
                                                "+",
                                                UnaryOp(
                                                    "+",
                                                    UnaryOp(
                                                        "+",
                                                        UnaryOp(
                                                            "+",
                                                            UnaryOp(
                                                                "-",
                                                                UnaryOp(
                                                                    "-",
                                                                    StringLiteral(
                                                                        '"1"'
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        VarDecl(
                                            Id("sth2"),
                                            ArrayType(9999, ClassType(Id("chaos"))),
                                            UnaryOp(
                                                "-",
                                                UnaryOp(
                                                    "-",
                                                    UnaryOp(
                                                        "+",
                                                        UnaryOp(
                                                            "+",
                                                            UnaryOp(
                                                                "+",
                                                                UnaryOp(
                                                                    "+",
                                                                    UnaryOp(
                                                                        "-",
                                                                        UnaryOp(
                                                                            "-",
                                                                            UnaryOp(
                                                                                "-",
                                                                                Id(
                                                                                    "hehe"
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        VarDecl(
                                            Id("sth3"),
                                            FloatType(),
                                            UnaryOp(
                                                "-",
                                                UnaryOp(
                                                    "-",
                                                    UnaryOp(
                                                        "-",
                                                        UnaryOp(
                                                            "+",
                                                            ArrayCell(
                                                                UnaryOp(
                                                                    "-",
                                                                    UnaryOp(
                                                                        "+",
                                                                        UnaryOp(
                                                                            "-",
                                                                            UnaryOp(
                                                                                "+",
                                                                                ArrayCell(
                                                                                    FieldAccess(
                                                                                        CallExpr(
                                                                                            Id(
                                                                                                "g"
                                                                                            ),
                                                                                            Id(
                                                                                                "h"
                                                                                            ),
                                                                                            [],
                                                                                        ),
                                                                                        Id(
                                                                                            "ij"
                                                                                        ),
                                                                                    ),
                                                                                    IntLiteral(
                                                                                        12
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                                IntLiteral(34),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_index_exp_1(self):
        """index operator: [, ]"""
        input = """
            class Index {
                static type hehe = a[1], hehe2 = a.b[\"string\" + 1], hehe3 = a.b(11)[11 * 5e6 + a.b[1e5 + c.d[2]]];
                string hehe4 = \"haha\"[10], hehe5 = {1,2,3}[2], hehe6 = false[7] + 1.e+9[8];
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Index"),
                        [
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("hehe"),
                                    ClassType(Id("type")),
                                    ArrayCell(Id("a"), IntLiteral(1)),
                                ),
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("hehe2"),
                                    ClassType(Id("type")),
                                    ArrayCell(
                                        FieldAccess(Id("a"), Id("b")),
                                        BinaryOp(
                                            "+",
                                            StringLiteral('"string"'),
                                            IntLiteral(1),
                                        ),
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("hehe3"),
                                    ClassType(Id("type")),
                                    ArrayCell(
                                        CallExpr(Id("a"), Id("b"), [IntLiteral(11)]),
                                        BinaryOp(
                                            "+",
                                            BinaryOp(
                                                "*",
                                                IntLiteral(11),
                                                FloatLiteral(5000000.0),
                                            ),
                                            ArrayCell(
                                                FieldAccess(Id("a"), Id("b")),
                                                BinaryOp(
                                                    "+",
                                                    FloatLiteral(100000.0),
                                                    ArrayCell(
                                                        FieldAccess(Id("c"), Id("d")),
                                                        IntLiteral(2),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("hehe4"),
                                    StringType(),
                                    ArrayCell(StringLiteral('"haha"'), IntLiteral(10)),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("hehe5"),
                                    StringType(),
                                    ArrayCell(
                                        ArrayLiteral(
                                            [
                                                IntLiteral(1),
                                                IntLiteral(2),
                                                IntLiteral(3),
                                            ]
                                        ),
                                        IntLiteral(2),
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("hehe6"),
                                    StringType(),
                                    BinaryOp(
                                        "+",
                                        ArrayCell(BooleanLiteral(False), IntLiteral(7)),
                                        ArrayCell(
                                            FloatLiteral(1000000000.0), IntLiteral(8)
                                        ),
                                    ),
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_index_exp_2(self):
        """index operator: [, ]"""
        input = """
            class Index {
                type hehe = a.b.c()[1], hehe2 = d.e.f[2];
                int call() {
                    final Class obj = new Class((a.b.c).thia.null[10], nil[false[1]]), obj2 = a[b[c[d[e[f[g.h(\"j\"[1])]]]]]];
                    a.b[2] := a.b()[3];
                    a[3[1] ^ a.b(2)] := a[b[99 % 8e5]] +3;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Index"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("hehe"),
                                    ClassType(Id("type")),
                                    ArrayCell(
                                        CallExpr(
                                            FieldAccess(Id("a"), Id("b")), Id("c"), []
                                        ),
                                        IntLiteral(1),
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("hehe2"),
                                    ClassType(Id("type")),
                                    ArrayCell(
                                        FieldAccess(
                                            FieldAccess(Id("d"), Id("e")), Id("f")
                                        ),
                                        IntLiteral(2),
                                    ),
                                ),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        ConstDecl(
                                            Id("obj"),
                                            ClassType(Id("Class")),
                                            NewExpr(
                                                Id("Class"),
                                                [
                                                    ArrayCell(
                                                        FieldAccess(
                                                            FieldAccess(
                                                                FieldAccess(
                                                                    FieldAccess(
                                                                        Id("a"), Id("b")
                                                                    ),
                                                                    Id("c"),
                                                                ),
                                                                Id("thia"),
                                                            ),
                                                            Id("null"),
                                                        ),
                                                        IntLiteral(10),
                                                    ),
                                                    ArrayCell(
                                                        NullLiteral(),
                                                        ArrayCell(
                                                            BooleanLiteral(False),
                                                            IntLiteral(1),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        ConstDecl(
                                            Id("obj2"),
                                            ClassType(Id("Class")),
                                            ArrayCell(
                                                Id("a"),
                                                ArrayCell(
                                                    Id("b"),
                                                    ArrayCell(
                                                        Id("c"),
                                                        ArrayCell(
                                                            Id("d"),
                                                            ArrayCell(
                                                                Id("e"),
                                                                ArrayCell(
                                                                    Id("f"),
                                                                    CallExpr(
                                                                        Id("g"),
                                                                        Id("h"),
                                                                        [
                                                                            ArrayCell(
                                                                                StringLiteral(
                                                                                    '"j"'
                                                                                ),
                                                                                IntLiteral(
                                                                                    1
                                                                                ),
                                                                            )
                                                                        ],
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ],
                                    [
                                        Assign(
                                            ArrayCell(
                                                FieldAccess(Id("a"), Id("b")),
                                                IntLiteral(2),
                                            ),
                                            ArrayCell(
                                                CallExpr(Id("a"), Id("b"), []),
                                                IntLiteral(3),
                                            ),
                                        ),
                                        Assign(
                                            ArrayCell(
                                                Id("a"),
                                                BinaryOp(
                                                    "^",
                                                    ArrayCell(
                                                        IntLiteral(3), IntLiteral(1)
                                                    ),
                                                    CallExpr(
                                                        Id("a"),
                                                        Id("b"),
                                                        [IntLiteral(2)],
                                                    ),
                                                ),
                                            ),
                                            BinaryOp(
                                                "+",
                                                ArrayCell(
                                                    Id("a"),
                                                    ArrayCell(
                                                        Id("b"),
                                                        BinaryOp(
                                                            "%",
                                                            IntLiteral(99),
                                                            FloatLiteral(800000.0),
                                                        ),
                                                    ),
                                                ),
                                                IntLiteral(3),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_attribute_access_1(self):
        """instance attribute access"""
        input = """
            class AttrAccess {
                string attr = f.g().h, attr2 = a.b.c().d, attr3 = (nil.e().f()).g;
                int call() {
                    Group a = new Group((i.j[9 + \"hehe\"]).k, (false + 6e9 ^ {\"obj\"}).obj.value);
                    int b = ({{19.1}}.b.c).d;
                    float c = new D().e;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("AttrAccess"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("attr"),
                                    StringType(),
                                    FieldAccess(
                                        CallExpr(Id("f"), Id("g"), []), Id("h")
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("attr2"),
                                    StringType(),
                                    FieldAccess(
                                        CallExpr(
                                            FieldAccess(Id("a"), Id("b")), Id("c"), []
                                        ),
                                        Id("d"),
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("attr3"),
                                    StringType(),
                                    FieldAccess(
                                        CallExpr(
                                            CallExpr(NullLiteral(), Id("e"), []),
                                            Id("f"),
                                            [],
                                        ),
                                        Id("g"),
                                    ),
                                ),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("a"),
                                            ClassType(Id("Group")),
                                            NewExpr(
                                                Id("Group"),
                                                [
                                                    FieldAccess(
                                                        ArrayCell(
                                                            FieldAccess(
                                                                Id("i"), Id("j")
                                                            ),
                                                            BinaryOp(
                                                                "+",
                                                                IntLiteral(9),
                                                                StringLiteral('"hehe"'),
                                                            ),
                                                        ),
                                                        Id("k"),
                                                    ),
                                                    FieldAccess(
                                                        FieldAccess(
                                                            BinaryOp(
                                                                "+",
                                                                BooleanLiteral(False),
                                                                BinaryOp(
                                                                    "^",
                                                                    FloatLiteral(
                                                                        6000000000.0
                                                                    ),
                                                                    ArrayLiteral(
                                                                        [
                                                                            StringLiteral(
                                                                                '"obj"'
                                                                            )
                                                                        ]
                                                                    ),
                                                                ),
                                                            ),
                                                            Id("obj"),
                                                        ),
                                                        Id("value"),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        VarDecl(
                                            Id("b"),
                                            IntType(),
                                            FieldAccess(
                                                FieldAccess(
                                                    FieldAccess(
                                                        ArrayLiteral(
                                                            [
                                                                ArrayLiteral(
                                                                    [FloatLiteral(19.1)]
                                                                )
                                                            ]
                                                        ),
                                                        Id("b"),
                                                    ),
                                                    Id("c"),
                                                ),
                                                Id("d"),
                                            ),
                                        ),
                                        VarDecl(
                                            Id("c"),
                                            FloatType(),
                                            FieldAccess(NewExpr(Id("D"), []), Id("e")),
                                        ),
                                    ],
                                    [],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_attribute_access_2(self):
        """static attribute access"""
        input = """
            class AttrAccess {
                string attr = g.h, attr2 = a.b.c.d, attr3 = this.e.f.g;
                int call() {
                    Group a = new Group(i.j.k, obj1.obj2.obj3.value);
                    int b = 19e1.b.c.d;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("AttrAccess"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("attr"),
                                    StringType(),
                                    FieldAccess(Id("g"), Id("h")),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("attr2"),
                                    StringType(),
                                    FieldAccess(
                                        FieldAccess(
                                            FieldAccess(Id("a"), Id("b")), Id("c")
                                        ),
                                        Id("d"),
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("attr3"),
                                    StringType(),
                                    FieldAccess(
                                        FieldAccess(
                                            FieldAccess(SelfLiteral(), Id("e")), Id("f")
                                        ),
                                        Id("g"),
                                    ),
                                ),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("a"),
                                            ClassType(Id("Group")),
                                            NewExpr(
                                                Id("Group"),
                                                [
                                                    FieldAccess(
                                                        FieldAccess(Id("i"), Id("j")),
                                                        Id("k"),
                                                    ),
                                                    FieldAccess(
                                                        FieldAccess(
                                                            FieldAccess(
                                                                Id("obj1"), Id("obj2")
                                                            ),
                                                            Id("obj3"),
                                                        ),
                                                        Id("value"),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        VarDecl(
                                            Id("b"),
                                            IntType(),
                                            FieldAccess(
                                                FieldAccess(
                                                    FieldAccess(
                                                        FloatLiteral(190.0), Id("b")
                                                    ),
                                                    Id("c"),
                                                ),
                                                Id("d"),
                                            ),
                                        ),
                                    ],
                                    [],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_method_invocation_1(self):
        """instace method invocation"""
        input = """
            class MethodInvoc {
                string temp = a.b().c(), temp2 = this.b().c(0, ({\"1\"} + \"f\" + a.F(hehe)));
                int call() {
                    bool[2] hehe = ((\"return obj\"[1] ^ !nil)[12] + false + {1,2e4,3}).method(nil, param[false]);
                    int b = (19.e1.b.c).d();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("MethodInvoc"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("temp"),
                                    StringType(),
                                    CallExpr(
                                        CallExpr(Id("a"), Id("b"), []), Id("c"), []
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("temp2"),
                                    StringType(),
                                    CallExpr(
                                        CallExpr(SelfLiteral(), Id("b"), []),
                                        Id("c"),
                                        [
                                            IntLiteral(0),
                                            BinaryOp(
                                                "+",
                                                BinaryOp(
                                                    "+",
                                                    ArrayLiteral(
                                                        [StringLiteral('"1"')]
                                                    ),
                                                    StringLiteral('"f"'),
                                                ),
                                                CallExpr(
                                                    Id("a"), Id("F"), [Id("hehe")]
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("hehe"),
                                            ArrayType(2, ClassType(Id("bool"))),
                                            CallExpr(
                                                BinaryOp(
                                                    "+",
                                                    BinaryOp(
                                                        "+",
                                                        ArrayCell(
                                                            BinaryOp(
                                                                "^",
                                                                ArrayCell(
                                                                    StringLiteral(
                                                                        '"return obj"'
                                                                    ),
                                                                    IntLiteral(1),
                                                                ),
                                                                UnaryOp(
                                                                    "!", NullLiteral()
                                                                ),
                                                            ),
                                                            IntLiteral(12),
                                                        ),
                                                        BooleanLiteral(False),
                                                    ),
                                                    ArrayLiteral(
                                                        [
                                                            IntLiteral(1),
                                                            FloatLiteral(20000.0),
                                                            IntLiteral(3),
                                                        ]
                                                    ),
                                                ),
                                                Id("method"),
                                                [
                                                    NullLiteral(),
                                                    ArrayCell(
                                                        Id("param"),
                                                        BooleanLiteral(False),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        VarDecl(
                                            Id("b"),
                                            IntType(),
                                            CallExpr(
                                                FieldAccess(
                                                    FieldAccess(
                                                        FloatLiteral(190.0), Id("b")
                                                    ),
                                                    Id("c"),
                                                ),
                                                Id("d"),
                                                [],
                                            ),
                                        ),
                                    ],
                                    [],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_method_invocation_2(self):
        """static method invocation"""
        input = """
            class MethodInvoc {
                string temp = a.b.c.d(), temp2 = e.f.g(1,{3} + 9,\"3\");
                int call() {
                    final type[3000] temp3 = new type(this, (k.l(h.i(a[2 ^ a.b[x % y % \"z\"]], bleh), k+1+!false, l.m(n, {\"o\"}))));
                    int b = 19.1.b.c.d(), c = new D().e();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("MethodInvoc"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("temp"),
                                    StringType(),
                                    CallExpr(
                                        FieldAccess(
                                            FieldAccess(Id("a"), Id("b")), Id("c")
                                        ),
                                        Id("d"),
                                        [],
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("temp2"),
                                    StringType(),
                                    CallExpr(
                                        FieldAccess(Id("e"), Id("f")),
                                        Id("g"),
                                        [
                                            IntLiteral(1),
                                            BinaryOp(
                                                "+",
                                                ArrayLiteral([IntLiteral(3)]),
                                                IntLiteral(9),
                                            ),
                                            StringLiteral('"3"'),
                                        ],
                                    ),
                                ),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        ConstDecl(
                                            Id("temp3"),
                                            ArrayType(3000, ClassType(Id("type"))),
                                            NewExpr(
                                                Id("type"),
                                                [
                                                    SelfLiteral(),
                                                    CallExpr(
                                                        Id("k"),
                                                        Id("l"),
                                                        [
                                                            CallExpr(
                                                                Id("h"),
                                                                Id("i"),
                                                                [
                                                                    ArrayCell(
                                                                        Id("a"),
                                                                        BinaryOp(
                                                                            "^",
                                                                            IntLiteral(
                                                                                2
                                                                            ),
                                                                            ArrayCell(
                                                                                FieldAccess(
                                                                                    Id(
                                                                                        "a"
                                                                                    ),
                                                                                    Id(
                                                                                        "b"
                                                                                    ),
                                                                                ),
                                                                                BinaryOp(
                                                                                    "%",
                                                                                    BinaryOp(
                                                                                        "%",
                                                                                        Id(
                                                                                            "x"
                                                                                        ),
                                                                                        Id(
                                                                                            "y"
                                                                                        ),
                                                                                    ),
                                                                                    StringLiteral(
                                                                                        '"z"'
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                    Id("bleh"),
                                                                ],
                                                            ),
                                                            BinaryOp(
                                                                "+",
                                                                BinaryOp(
                                                                    "+",
                                                                    Id("k"),
                                                                    IntLiteral(1),
                                                                ),
                                                                UnaryOp(
                                                                    "!",
                                                                    BooleanLiteral(
                                                                        False
                                                                    ),
                                                                ),
                                                            ),
                                                            CallExpr(
                                                                Id("l"),
                                                                Id("m"),
                                                                [
                                                                    Id("n"),
                                                                    ArrayLiteral(
                                                                        [
                                                                            StringLiteral(
                                                                                '"o"'
                                                                            )
                                                                        ]
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ),
                                        VarDecl(
                                            Id("b"),
                                            IntType(),
                                            CallExpr(
                                                FieldAccess(
                                                    FieldAccess(
                                                        FloatLiteral(19.1), Id("b")
                                                    ),
                                                    Id("c"),
                                                ),
                                                Id("d"),
                                                [],
                                            ),
                                        ),
                                        VarDecl(
                                            Id("c"),
                                            IntType(),
                                            CallExpr(NewExpr(Id("D"), []), Id("e"), []),
                                        ),
                                    ],
                                    [],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_object_creation(self):
        """new"""
        input = """
            class Y extends X {
                A a = new B();
                int call() {
                    x x = new A(), x2 = new B(new C(1, 2), new D(true, {1, 2, {{3}}}, nil), this, hehe);
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Y"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("a"), ClassType(Id("A")), NewExpr(Id("B"), [])
                                ),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("x"),
                                            ClassType(Id("x")),
                                            NewExpr(Id("A"), []),
                                        ),
                                        VarDecl(
                                            Id("x2"),
                                            ClassType(Id("x")),
                                            NewExpr(
                                                Id("B"),
                                                [
                                                    NewExpr(
                                                        Id("C"),
                                                        [IntLiteral(1), IntLiteral(2)],
                                                    ),
                                                    NewExpr(
                                                        Id("D"),
                                                        [
                                                            BooleanLiteral(True),
                                                            ArrayLiteral(
                                                                [
                                                                    IntLiteral(1),
                                                                    IntLiteral(2),
                                                                    ArrayLiteral(
                                                                        [
                                                                            ArrayLiteral(
                                                                                [
                                                                                    IntLiteral(
                                                                                        3
                                                                                    )
                                                                                ]
                                                                            )
                                                                        ]
                                                                    ),
                                                                ]
                                                            ),
                                                            NullLiteral(),
                                                        ],
                                                    ),
                                                    SelfLiteral(),
                                                    Id("hehe"),
                                                ],
                                            ),
                                        ),
                                    ],
                                    [],
                                ),
                            ),
                        ],
                        Id("X"),
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_all_exp_1(self):
        """mixed expressions"""
        input = """
            class Exp {
                A a = new C(new B()), a2 = new D({1} * new D());
                static int b = e.f.g, c = b[99] ^ 10 * (Math.pow(2, c));
                int main() {
                    var1 res = !9 * 8 + a.b && (new A( 1 || 2)).d .c;
                    char[100] tmp = \"1\" ^ {22} ^ (d.e()[\"9\" ^ y]).f({\"lala\"}, hehe) % new X(hehe);
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Exp"),
                        [
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("a"),
                                    ClassType(Id("A")),
                                    NewExpr(Id("C"), [NewExpr(Id("B"), [])]),
                                ),
                            ),
                            AttributeDecl(
                                Instance(),
                                VarDecl(
                                    Id("a2"),
                                    ClassType(Id("A")),
                                    NewExpr(
                                        Id("D"),
                                        [
                                            BinaryOp(
                                                "*",
                                                ArrayLiteral([IntLiteral(1)]),
                                                NewExpr(Id("D"), []),
                                            )
                                        ],
                                    ),
                                ),
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("b"),
                                    IntType(),
                                    FieldAccess(FieldAccess(Id("e"), Id("f")), Id("g")),
                                ),
                            ),
                            AttributeDecl(
                                Static(),
                                VarDecl(
                                    Id("c"),
                                    IntType(),
                                    BinaryOp(
                                        "*",
                                        BinaryOp(
                                            "^",
                                            ArrayCell(Id("b"), IntLiteral(99)),
                                            IntLiteral(10),
                                        ),
                                        CallExpr(
                                            Id("Math"),
                                            Id("pow"),
                                            [IntLiteral(2), Id("c")],
                                        ),
                                    ),
                                ),
                            ),
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("res"),
                                            ClassType(Id("var1")),
                                            BinaryOp(
                                                "&&",
                                                BinaryOp(
                                                    "+",
                                                    BinaryOp(
                                                        "*",
                                                        UnaryOp("!", IntLiteral(9)),
                                                        IntLiteral(8),
                                                    ),
                                                    FieldAccess(Id("a"), Id("b")),
                                                ),
                                                FieldAccess(
                                                    FieldAccess(
                                                        NewExpr(
                                                            Id("A"),
                                                            [
                                                                BinaryOp(
                                                                    "||",
                                                                    IntLiteral(1),
                                                                    IntLiteral(2),
                                                                )
                                                            ],
                                                        ),
                                                        Id("d"),
                                                    ),
                                                    Id("c"),
                                                ),
                                            ),
                                        ),
                                        VarDecl(
                                            Id("tmp"),
                                            ArrayType(100, ClassType(Id("char"))),
                                            BinaryOp(
                                                "%",
                                                BinaryOp(
                                                    "^",
                                                    BinaryOp(
                                                        "^",
                                                        StringLiteral('"1"'),
                                                        ArrayLiteral([IntLiteral(22)]),
                                                    ),
                                                    CallExpr(
                                                        ArrayCell(
                                                            CallExpr(
                                                                Id("d"), Id("e"), []
                                                            ),
                                                            BinaryOp(
                                                                "^",
                                                                StringLiteral('"9"'),
                                                                Id("y"),
                                                            ),
                                                        ),
                                                        Id("f"),
                                                        [
                                                            ArrayLiteral(
                                                                [
                                                                    StringLiteral(
                                                                        '"lala"'
                                                                    )
                                                                ]
                                                            ),
                                                            Id("hehe"),
                                                        ],
                                                    ),
                                                ),
                                                NewExpr(Id("X"), [Id("hehe")]),
                                            ),
                                        ),
                                    ],
                                    [],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_all_exp_2(self):
        """mixed expressions"""
        input = """
            class Exp {
                int main() {
                    Any complex1 = !this.b(9 + 8e+6 <= 9 - {7} + 6 - \"5\") && false * !-+true + !--+-+\"string\" && new A((1 != !1..a) == \"a[1]\") || nil.hehe;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Exp"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("complex1"),
                                            ClassType(Id("Any")),
                                            BinaryOp(
                                                "||",
                                                BinaryOp(
                                                    "&&",
                                                    BinaryOp(
                                                        "&&",
                                                        UnaryOp(
                                                            "!",
                                                            CallExpr(
                                                                SelfLiteral(),
                                                                Id("b"),
                                                                [
                                                                    BinaryOp(
                                                                        "<=",
                                                                        BinaryOp(
                                                                            "+",
                                                                            IntLiteral(
                                                                                9
                                                                            ),
                                                                            FloatLiteral(
                                                                                8000000.0
                                                                            ),
                                                                        ),
                                                                        BinaryOp(
                                                                            "-",
                                                                            BinaryOp(
                                                                                "+",
                                                                                BinaryOp(
                                                                                    "-",
                                                                                    IntLiteral(
                                                                                        9
                                                                                    ),
                                                                                    ArrayLiteral(
                                                                                        [
                                                                                            IntLiteral(
                                                                                                7
                                                                                            )
                                                                                        ]
                                                                                    ),
                                                                                ),
                                                                                IntLiteral(
                                                                                    6
                                                                                ),
                                                                            ),
                                                                            StringLiteral(
                                                                                '"5"'
                                                                            ),
                                                                        ),
                                                                    )
                                                                ],
                                                            ),
                                                        ),
                                                        BinaryOp(
                                                            "+",
                                                            BinaryOp(
                                                                "*",
                                                                BooleanLiteral(False),
                                                                UnaryOp(
                                                                    "!",
                                                                    UnaryOp(
                                                                        "-",
                                                                        UnaryOp(
                                                                            "+",
                                                                            BooleanLiteral(
                                                                                True
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                            UnaryOp(
                                                                "!",
                                                                UnaryOp(
                                                                    "-",
                                                                    UnaryOp(
                                                                        "-",
                                                                        UnaryOp(
                                                                            "+",
                                                                            UnaryOp(
                                                                                "-",
                                                                                UnaryOp(
                                                                                    "+",
                                                                                    StringLiteral(
                                                                                        '"string"'
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                    NewExpr(
                                                        Id("A"),
                                                        [
                                                            BinaryOp(
                                                                "==",
                                                                BinaryOp(
                                                                    "!=",
                                                                    IntLiteral(1),
                                                                    UnaryOp(
                                                                        "!",
                                                                        FieldAccess(
                                                                            FloatLiteral(
                                                                                1.0
                                                                            ),
                                                                            Id("a"),
                                                                        ),
                                                                    ),
                                                                ),
                                                                StringLiteral('"a[1]"'),
                                                            )
                                                        ],
                                                    ),
                                                ),
                                                FieldAccess(NullLiteral(), Id("hehe")),
                                            ),
                                        )
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_all_exp_3(self):
        """mixed expression"""
        input = """
            class Exp {
                static int main() {
                    final Any [100] complex2 = -+nil * new d1(new d2(this[3]) || 0 && 1 || False).a / 18 \\ 0072.e+0 + 10 * (a.b).a[3] % 999 - !8[8 + \"8\"] ^ {0.2} ^ !-this ^ +T != 1 ^ (2 ^ false ^ new E().a.b[-4 % 6 % (9[10])[{\"11\", 1e-2}]] ^ {3e4} > \"45\");
                }
            }
            
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Exp"),
                        [
                            MethodDecl(
                                Static(),
                                Id("main"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        ConstDecl(
                                            Id("complex2"),
                                            ArrayType(100, ClassType(Id("Any"))),
                                            BinaryOp(
                                                "!=",
                                                BinaryOp(
                                                    "-",
                                                    BinaryOp(
                                                        "+",
                                                        BinaryOp(
                                                            "\\",
                                                            BinaryOp(
                                                                "/",
                                                                BinaryOp(
                                                                    "*",
                                                                    UnaryOp(
                                                                        "-",
                                                                        UnaryOp(
                                                                            "+",
                                                                            NullLiteral(),
                                                                        ),
                                                                    ),
                                                                    FieldAccess(
                                                                        NewExpr(
                                                                            Id("d1"),
                                                                            [
                                                                                BinaryOp(
                                                                                    "||",
                                                                                    BinaryOp(
                                                                                        "&&",
                                                                                        BinaryOp(
                                                                                            "||",
                                                                                            NewExpr(
                                                                                                Id(
                                                                                                    "d2"
                                                                                                ),
                                                                                                [
                                                                                                    ArrayCell(
                                                                                                        SelfLiteral(),
                                                                                                        IntLiteral(
                                                                                                            3
                                                                                                        ),
                                                                                                    )
                                                                                                ],
                                                                                            ),
                                                                                            IntLiteral(
                                                                                                0
                                                                                            ),
                                                                                        ),
                                                                                        IntLiteral(
                                                                                            1
                                                                                        ),
                                                                                    ),
                                                                                    Id(
                                                                                        "False"
                                                                                    ),
                                                                                )
                                                                            ],
                                                                        ),
                                                                        Id("a"),
                                                                    ),
                                                                ),
                                                                IntLiteral(18),
                                                            ),
                                                            FloatLiteral(72.0),
                                                        ),
                                                        BinaryOp(
                                                            "%",
                                                            BinaryOp(
                                                                "*",
                                                                IntLiteral(10),
                                                                ArrayCell(
                                                                    FieldAccess(
                                                                        FieldAccess(
                                                                            Id("a"),
                                                                            Id("b"),
                                                                        ),
                                                                        Id("a"),
                                                                    ),
                                                                    IntLiteral(3),
                                                                ),
                                                            ),
                                                            IntLiteral(999),
                                                        ),
                                                    ),
                                                    BinaryOp(
                                                        "^",
                                                        BinaryOp(
                                                            "^",
                                                            BinaryOp(
                                                                "^",
                                                                UnaryOp(
                                                                    "!",
                                                                    ArrayCell(
                                                                        IntLiteral(8),
                                                                        BinaryOp(
                                                                            "+",
                                                                            IntLiteral(
                                                                                8
                                                                            ),
                                                                            StringLiteral(
                                                                                '"8"'
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                                ArrayLiteral(
                                                                    [FloatLiteral(0.2)]
                                                                ),
                                                            ),
                                                            UnaryOp(
                                                                "!",
                                                                UnaryOp(
                                                                    "-", SelfLiteral()
                                                                ),
                                                            ),
                                                        ),
                                                        UnaryOp("+", Id("T")),
                                                    ),
                                                ),
                                                BinaryOp(
                                                    "^",
                                                    IntLiteral(1),
                                                    BinaryOp(
                                                        ">",
                                                        BinaryOp(
                                                            "^",
                                                            BinaryOp(
                                                                "^",
                                                                BinaryOp(
                                                                    "^",
                                                                    IntLiteral(2),
                                                                    BooleanLiteral(
                                                                        False
                                                                    ),
                                                                ),
                                                                ArrayCell(
                                                                    FieldAccess(
                                                                        FieldAccess(
                                                                            NewExpr(
                                                                                Id("E"),
                                                                                [],
                                                                            ),
                                                                            Id("a"),
                                                                        ),
                                                                        Id("b"),
                                                                    ),
                                                                    BinaryOp(
                                                                        "%",
                                                                        BinaryOp(
                                                                            "%",
                                                                            UnaryOp(
                                                                                "-",
                                                                                IntLiteral(
                                                                                    4
                                                                                ),
                                                                            ),
                                                                            IntLiteral(
                                                                                6
                                                                            ),
                                                                        ),
                                                                        ArrayCell(
                                                                            ArrayCell(
                                                                                IntLiteral(
                                                                                    9
                                                                                ),
                                                                                IntLiteral(
                                                                                    10
                                                                                ),
                                                                            ),
                                                                            ArrayLiteral(
                                                                                [
                                                                                    StringLiteral(
                                                                                        '"11"'
                                                                                    ),
                                                                                    FloatLiteral(
                                                                                        0.01
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                            ArrayLiteral(
                                                                [FloatLiteral(30000.0)]
                                                            ),
                                                        ),
                                                        StringLiteral('"45"'),
                                                    ),
                                                ),
                                            ),
                                        )
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 367))

    """3. STATEMENT"""

    def test_simple_block_statement_1(self):
        """block with variable declaraions"""
        input = """
            class Stmt {
                int main() {
                    bool zero, oclock;
                    int minute = 60, hour = 12;
                    float[99] sec = new Boolean();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(Id("zero"), ClassType(Id("bool"))),
                                        VarDecl(Id("oclock"), ClassType(Id("bool"))),
                                        VarDecl(
                                            Id("minute"), IntType(), IntLiteral(60)
                                        ),
                                        VarDecl(Id("hour"), IntType(), IntLiteral(12)),
                                        VarDecl(
                                            Id("sec"),
                                            ArrayType(99, FloatType()),
                                            NewExpr(Id("Boolean"), []),
                                        ),
                                    ],
                                    [],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_simple_block_statement_2(self):
        """blocks with statements"""
        input = """
            class Stmt {
                int main() {
                    s:=r*r*this.myPI;
                    a[0]:= s;
                    return null ^ nil;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        Assign(
                                            Id("s"),
                                            BinaryOp(
                                                "*",
                                                BinaryOp("*", Id("r"), Id("r")),
                                                FieldAccess(SelfLiteral(), Id("myPI")),
                                            ),
                                        ),
                                        Assign(
                                            ArrayCell(Id("a"), IntLiteral(0)), Id("s")
                                        ),
                                        Return(
                                            BinaryOp("^", Id("null"), NullLiteral())
                                        ),
                                    ],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_simple_block_statement_3(self):
        """blocks with variable declarations & statements"""
        input = """
            class Stmt {
                string temp;
                int call() {
                    float num = 99, q = \"fall\", r;
                    bool b, d = e.f.g;
                    single_block[8] := hehe + d.e[3];
                    if true then {
                        a.b();
                    }
                    else
                        a.c();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(Id("num"), FloatType(), IntLiteral(99)),
                                        VarDecl(
                                            Id("q"),
                                            FloatType(),
                                            StringLiteral('"fall"'),
                                        ),
                                        VarDecl(Id("r"), FloatType()),
                                        VarDecl(Id("b"), ClassType(Id("bool"))),
                                        VarDecl(
                                            Id("d"),
                                            ClassType(Id("bool")),
                                            FieldAccess(
                                                FieldAccess(Id("e"), Id("f")), Id("g")
                                            ),
                                        ),
                                    ],
                                    [
                                        Assign(
                                            ArrayCell(
                                                Id("single_block"), IntLiteral(8)
                                            ),
                                            BinaryOp(
                                                "+",
                                                Id("hehe"),
                                                ArrayCell(
                                                    FieldAccess(Id("d"), Id("e")),
                                                    IntLiteral(3),
                                                ),
                                            ),
                                        ),
                                        If(
                                            BooleanLiteral(True),
                                            Block([], [CallStmt(Id("a"), Id("b"), [])]),
                                            CallStmt(Id("a"), Id("c"), []),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_advanced_block_statement_1(self):
        """nested blocks"""
        input = """
            class Mixed {
                static method1() {{{}{{{{}{
                    for i := 1 to 10 do {
                        {}{{{}{}}}
                        if a then
                            {{}{}{{}}}
                        else {{{{}}}{}{}}
                    }
                }{}}{}}{}}}}
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Mixed"),
                        [
                            MethodDecl(
                                Static(),
                                Id("<init>"),
                                [],
                                None,
                                Block(
                                    [],
                                    [
                                        Block(
                                            [],
                                            [
                                                Block([], []),
                                                Block(
                                                    [],
                                                    [
                                                        Block(
                                                            [],
                                                            [
                                                                Block(
                                                                    [],
                                                                    [
                                                                        Block([], []),
                                                                        Block(
                                                                            [],
                                                                            [
                                                                                For(
                                                                                    Id(
                                                                                        "i"
                                                                                    ),
                                                                                    IntLiteral(
                                                                                        1
                                                                                    ),
                                                                                    IntLiteral(
                                                                                        10
                                                                                    ),
                                                                                    True,
                                                                                    Block(
                                                                                        [],
                                                                                        [
                                                                                            Block(
                                                                                                [],
                                                                                                [],
                                                                                            ),
                                                                                            Block(
                                                                                                [],
                                                                                                [
                                                                                                    Block(
                                                                                                        [],
                                                                                                        [
                                                                                                            Block(
                                                                                                                [],
                                                                                                                [],
                                                                                                            ),
                                                                                                            Block(
                                                                                                                [],
                                                                                                                [],
                                                                                                            ),
                                                                                                        ],
                                                                                                    )
                                                                                                ],
                                                                                            ),
                                                                                            If(
                                                                                                Id(
                                                                                                    "a"
                                                                                                ),
                                                                                                Block(
                                                                                                    [],
                                                                                                    [
                                                                                                        Block(
                                                                                                            [],
                                                                                                            [],
                                                                                                        ),
                                                                                                        Block(
                                                                                                            [],
                                                                                                            [],
                                                                                                        ),
                                                                                                        Block(
                                                                                                            [],
                                                                                                            [
                                                                                                                Block(
                                                                                                                    [],
                                                                                                                    [],
                                                                                                                )
                                                                                                            ],
                                                                                                        ),
                                                                                                    ],
                                                                                                ),
                                                                                                Block(
                                                                                                    [],
                                                                                                    [
                                                                                                        Block(
                                                                                                            [],
                                                                                                            [
                                                                                                                Block(
                                                                                                                    [],
                                                                                                                    [
                                                                                                                        Block(
                                                                                                                            [],
                                                                                                                            [],
                                                                                                                        )
                                                                                                                    ],
                                                                                                                )
                                                                                                            ],
                                                                                                        ),
                                                                                                        Block(
                                                                                                            [],
                                                                                                            [],
                                                                                                        ),
                                                                                                        Block(
                                                                                                            [],
                                                                                                            [],
                                                                                                        ),
                                                                                                    ],
                                                                                                ),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                )
                                                                            ],
                                                                        ),
                                                                        Block([], []),
                                                                    ],
                                                                ),
                                                                Block([], []),
                                                            ],
                                                        ),
                                                        Block([], []),
                                                    ],
                                                ),
                                            ],
                                        )
                                    ],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_advanced_block_statement_2(self):
        """nested blocks"""
        input = """
            class Mixed {
                bool method2() {
                    bool a, b;
                    int c, d, e = 100e0;
                    {
                        {
                            strin[10] a, b, c, d;
                            {
                                (this.a.b()[9]).c();
                            }
                        }
                        {
                            int[10] a, b = g.h[10];
                            float c = 070029.e-543;
                            non_local d;
                            {
                                local e = {nil, false};
                            }
                            return (this.a).b.c;
                        }
                    }
                    return something[20] * !-+\"haha\";
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Mixed"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("method2"),
                                [],
                                ClassType(Id("bool")),
                                Block(
                                    [
                                        VarDecl(Id("a"), ClassType(Id("bool"))),
                                        VarDecl(Id("b"), ClassType(Id("bool"))),
                                        VarDecl(Id("c"), IntType()),
                                        VarDecl(Id("d"), IntType()),
                                        VarDecl(
                                            Id("e"), IntType(), FloatLiteral(100.0)
                                        ),
                                    ],
                                    [
                                        Block(
                                            [],
                                            [
                                                Block(
                                                    [
                                                        VarDecl(
                                                            Id("a"),
                                                            ArrayType(
                                                                10,
                                                                ClassType(Id("strin")),
                                                            ),
                                                        ),
                                                        VarDecl(
                                                            Id("b"),
                                                            ArrayType(
                                                                10,
                                                                ClassType(Id("strin")),
                                                            ),
                                                        ),
                                                        VarDecl(
                                                            Id("c"),
                                                            ArrayType(
                                                                10,
                                                                ClassType(Id("strin")),
                                                            ),
                                                        ),
                                                        VarDecl(
                                                            Id("d"),
                                                            ArrayType(
                                                                10,
                                                                ClassType(Id("strin")),
                                                            ),
                                                        ),
                                                    ],
                                                    [
                                                        Block(
                                                            [],
                                                            [
                                                                CallStmt(
                                                                    ArrayCell(
                                                                        CallExpr(
                                                                            FieldAccess(
                                                                                SelfLiteral(),
                                                                                Id("a"),
                                                                            ),
                                                                            Id("b"),
                                                                            [],
                                                                        ),
                                                                        IntLiteral(9),
                                                                    ),
                                                                    Id("c"),
                                                                    [],
                                                                )
                                                            ],
                                                        )
                                                    ],
                                                ),
                                                Block(
                                                    [
                                                        VarDecl(
                                                            Id("a"),
                                                            ArrayType(10, IntType()),
                                                        ),
                                                        VarDecl(
                                                            Id("b"),
                                                            ArrayType(10, IntType()),
                                                            ArrayCell(
                                                                FieldAccess(
                                                                    Id("g"), Id("h")
                                                                ),
                                                                IntLiteral(10),
                                                            ),
                                                        ),
                                                        VarDecl(
                                                            Id("c"),
                                                            FloatType(),
                                                            FloatLiteral(0.0),
                                                        ),
                                                        VarDecl(
                                                            Id("d"),
                                                            ClassType(Id("non_local")),
                                                        ),
                                                    ],
                                                    [
                                                        Block(
                                                            [
                                                                VarDecl(
                                                                    Id("e"),
                                                                    ClassType(
                                                                        Id("local")
                                                                    ),
                                                                    ArrayLiteral(
                                                                        [
                                                                            NullLiteral(),
                                                                            BooleanLiteral(
                                                                                False
                                                                            ),
                                                                        ]
                                                                    ),
                                                                )
                                                            ],
                                                            [],
                                                        ),
                                                        Return(
                                                            FieldAccess(
                                                                FieldAccess(
                                                                    FieldAccess(
                                                                        SelfLiteral(),
                                                                        Id("a"),
                                                                    ),
                                                                    Id("b"),
                                                                ),
                                                                Id("c"),
                                                            )
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        Return(
                                            BinaryOp(
                                                "*",
                                                ArrayCell(
                                                    Id("something"), IntLiteral(20)
                                                ),
                                                UnaryOp(
                                                    "!",
                                                    UnaryOp(
                                                        "-",
                                                        UnaryOp(
                                                            "+", StringLiteral('"haha"')
                                                        ),
                                                    ),
                                                ),
                                            )
                                        ),
                                    ],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_simple_assignment_statement_1(self):
        """lhs: variables"""
        input = """
            class Stmt {
                string temp;
                int call() {
                    var a, b, c = this;
                    a := 1;
                    b := nil % 1212 ^ !+\"this is a string\" / -a.b.d() * true \\ 53.e+80 ^ \"9\";
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(Id("a"), ClassType(Id("var"))),
                                        VarDecl(Id("b"), ClassType(Id("var"))),
                                        VarDecl(
                                            Id("c"), ClassType(Id("var")), SelfLiteral()
                                        ),
                                    ],
                                    [
                                        Assign(Id("a"), IntLiteral(1)),
                                        Assign(
                                            Id("b"),
                                            BinaryOp(
                                                "\\",
                                                BinaryOp(
                                                    "*",
                                                    BinaryOp(
                                                        "/",
                                                        BinaryOp(
                                                            "%",
                                                            NullLiteral(),
                                                            BinaryOp(
                                                                "^",
                                                                IntLiteral(1212),
                                                                UnaryOp(
                                                                    "!",
                                                                    UnaryOp(
                                                                        "+",
                                                                        StringLiteral(
                                                                            '"this is a string"'
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                        UnaryOp(
                                                            "-",
                                                            CallExpr(
                                                                FieldAccess(
                                                                    Id("a"), Id("b")
                                                                ),
                                                                Id("d"),
                                                                [],
                                                            ),
                                                        ),
                                                    ),
                                                    BooleanLiteral(True),
                                                ),
                                                BinaryOp(
                                                    "^",
                                                    FloatLiteral(5.3e81),
                                                    StringLiteral('"9"'),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_simple_assignment_statement_2(self):
        """lhs: mutable attributes"""
        input = """
            class Stmt {
                int main() {
                    obj1.method1(0).static_attr := \"integer\" == obj2 + 76 > false \\ hehe.hehe2[1] ^ new Sth2();
                    (obj2.method2(1)[99]).instance_attr := !-simple && true || +false == obj3;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        Assign(
                                            FieldAccess(
                                                CallExpr(
                                                    Id("obj1"),
                                                    Id("method1"),
                                                    [IntLiteral(0)],
                                                ),
                                                Id("static_attr"),
                                            ),
                                            BinaryOp(
                                                ">",
                                                BinaryOp(
                                                    "==",
                                                    StringLiteral('"integer"'),
                                                    BinaryOp(
                                                        "+", Id("obj2"), IntLiteral(76)
                                                    ),
                                                ),
                                                BinaryOp(
                                                    "\\",
                                                    BooleanLiteral(False),
                                                    BinaryOp(
                                                        "^",
                                                        ArrayCell(
                                                            FieldAccess(
                                                                Id("hehe"), Id("hehe2")
                                                            ),
                                                            IntLiteral(1),
                                                        ),
                                                        NewExpr(Id("Sth2"), []),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Assign(
                                            FieldAccess(
                                                ArrayCell(
                                                    CallExpr(
                                                        Id("obj2"),
                                                        Id("method2"),
                                                        [IntLiteral(1)],
                                                    ),
                                                    IntLiteral(99),
                                                ),
                                                Id("instance_attr"),
                                            ),
                                            BinaryOp(
                                                "==",
                                                BinaryOp(
                                                    "||",
                                                    BinaryOp(
                                                        "&&",
                                                        UnaryOp(
                                                            "!",
                                                            UnaryOp("-", Id("simple")),
                                                        ),
                                                        BooleanLiteral(True),
                                                    ),
                                                    UnaryOp("+", BooleanLiteral(False)),
                                                ),
                                                Id("obj3"),
                                            ),
                                        ),
                                    ],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_simple_assignment_statement_3(self):
        """lhs: indexing"""
        input = """
            class Stmt {
                string temp;
                int call() {
                    a.b.c.d[4] := new MethodInvoc();
                    o.p().q[5] := String ^ Float;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        Assign(
                                            ArrayCell(
                                                FieldAccess(
                                                    FieldAccess(
                                                        FieldAccess(Id("a"), Id("b")),
                                                        Id("c"),
                                                    ),
                                                    Id("d"),
                                                ),
                                                IntLiteral(4),
                                            ),
                                            NewExpr(Id("MethodInvoc"), []),
                                        ),
                                        Assign(
                                            ArrayCell(
                                                FieldAccess(
                                                    CallExpr(Id("o"), Id("p"), []),
                                                    Id("q"),
                                                ),
                                                IntLiteral(5),
                                            ),
                                            BinaryOp("^", Id("String"), Id("Float")),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_advanced_assignment_statement_1(self):
        """mixed assignment statements"""
        input = """
            class Mixed {
                string temp;
                int call() {
                    {
                        a := b[1];
                        {
                            res[1] := \"string\" % {4, 5, 6e7} * 8 == false / tru543 \\ 9;
                        }
                    }
                    b.e().d := hehe;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Mixed"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        Block(
                                            [],
                                            [
                                                Assign(
                                                    Id("a"),
                                                    ArrayCell(Id("b"), IntLiteral(1)),
                                                ),
                                                Block(
                                                    [],
                                                    [
                                                        Assign(
                                                            ArrayCell(
                                                                Id("res"), IntLiteral(1)
                                                            ),
                                                            BinaryOp(
                                                                "==",
                                                                BinaryOp(
                                                                    "*",
                                                                    BinaryOp(
                                                                        "%",
                                                                        StringLiteral(
                                                                            '"string"'
                                                                        ),
                                                                        ArrayLiteral(
                                                                            [
                                                                                IntLiteral(
                                                                                    4
                                                                                ),
                                                                                IntLiteral(
                                                                                    5
                                                                                ),
                                                                                FloatLiteral(
                                                                                    60000000.0
                                                                                ),
                                                                            ]
                                                                        ),
                                                                    ),
                                                                    IntLiteral(8),
                                                                ),
                                                                BinaryOp(
                                                                    "\\",
                                                                    BinaryOp(
                                                                        "/",
                                                                        BooleanLiteral(
                                                                            False
                                                                        ),
                                                                        Id("tru543"),
                                                                    ),
                                                                    IntLiteral(9),
                                                                ),
                                                            ),
                                                        )
                                                    ],
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            FieldAccess(
                                                CallExpr(Id("b"), Id("e"), []), Id("d")
                                            ),
                                            Id("hehe"),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_advanced_assignment_statement_2(self):
        """mixed assignment statements"""
        input = """
            class Mixed {
                int main () {
                    c := (a.b().c[2])[3] + new classA(new clB(param, {\"list\"}));
                    obj3.const_attr := x[a[b[c[d]]]] + g.h.i();
                    (e.f() + 9).a.b[x[0] + (x[1]).y()] := value + {{1}};
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Mixed"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        Assign(
                                            Id("c"),
                                            BinaryOp(
                                                "+",
                                                ArrayCell(
                                                    ArrayCell(
                                                        FieldAccess(
                                                            CallExpr(
                                                                Id("a"), Id("b"), []
                                                            ),
                                                            Id("c"),
                                                        ),
                                                        IntLiteral(2),
                                                    ),
                                                    IntLiteral(3),
                                                ),
                                                NewExpr(
                                                    Id("classA"),
                                                    [
                                                        NewExpr(
                                                            Id("clB"),
                                                            [
                                                                Id("param"),
                                                                ArrayLiteral(
                                                                    [
                                                                        StringLiteral(
                                                                            '"list"'
                                                                        )
                                                                    ]
                                                                ),
                                                            ],
                                                        )
                                                    ],
                                                ),
                                            ),
                                        ),
                                        Assign(
                                            FieldAccess(Id("obj3"), Id("const_attr")),
                                            BinaryOp(
                                                "+",
                                                ArrayCell(
                                                    Id("x"),
                                                    ArrayCell(
                                                        Id("a"),
                                                        ArrayCell(
                                                            Id("b"),
                                                            ArrayCell(Id("c"), Id("d")),
                                                        ),
                                                    ),
                                                ),
                                                CallExpr(
                                                    FieldAccess(Id("g"), Id("h")),
                                                    Id("i"),
                                                    [],
                                                ),
                                            ),
                                        ),
                                        Assign(
                                            ArrayCell(
                                                FieldAccess(
                                                    FieldAccess(
                                                        BinaryOp(
                                                            "+",
                                                            CallExpr(
                                                                Id("e"), Id("f"), []
                                                            ),
                                                            IntLiteral(9),
                                                        ),
                                                        Id("a"),
                                                    ),
                                                    Id("b"),
                                                ),
                                                BinaryOp(
                                                    "+",
                                                    ArrayCell(Id("x"), IntLiteral(0)),
                                                    CallExpr(
                                                        ArrayCell(
                                                            Id("x"), IntLiteral(1)
                                                        ),
                                                        Id("y"),
                                                        [],
                                                    ),
                                                ),
                                            ),
                                            BinaryOp(
                                                "+",
                                                Id("value"),
                                                ArrayLiteral(
                                                    [ArrayLiteral([IntLiteral(1)])]
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_if_statement_1(self):
        """if statement"""
        input = """
            class Stmt {
                string temp;
                int call() {
                    if (a) then
                        io.print(\"Hello \\\"world\\\"!\\n\");
                    if b then
                        if True || !-+true then
                            g.h.i()[9] := 10;
                        else
                            a.b().c[1] := nil.e() - false;
                    else
                        if exp then
                            doodoo.thing();
                    x := y.z();
                    return y.x();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        If(
                                            Id("a"),
                                            CallStmt(
                                                Id("io"),
                                                Id("print"),
                                                [
                                                    StringLiteral(
                                                        '"Hello \\"world\\"!\\n"'
                                                    )
                                                ],
                                            ),
                                        ),
                                        If(
                                            Id("b"),
                                            If(
                                                BinaryOp(
                                                    "||",
                                                    Id("True"),
                                                    UnaryOp(
                                                        "!",
                                                        UnaryOp(
                                                            "-",
                                                            UnaryOp(
                                                                "+",
                                                                BooleanLiteral(True),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                Assign(
                                                    ArrayCell(
                                                        CallExpr(
                                                            FieldAccess(
                                                                Id("g"), Id("h")
                                                            ),
                                                            Id("i"),
                                                            [],
                                                        ),
                                                        IntLiteral(9),
                                                    ),
                                                    IntLiteral(10),
                                                ),
                                                Assign(
                                                    ArrayCell(
                                                        FieldAccess(
                                                            CallExpr(
                                                                Id("a"), Id("b"), []
                                                            ),
                                                            Id("c"),
                                                        ),
                                                        IntLiteral(1),
                                                    ),
                                                    BinaryOp(
                                                        "-",
                                                        CallExpr(
                                                            NullLiteral(), Id("e"), []
                                                        ),
                                                        BooleanLiteral(False),
                                                    ),
                                                ),
                                            ),
                                            If(
                                                Id("exp"),
                                                CallStmt(Id("doodoo"), Id("thing"), []),
                                            ),
                                        ),
                                        Assign(Id("x"), CallExpr(Id("y"), Id("z"), [])),
                                        Return(CallExpr(Id("y"), Id("x"), [])),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_if_statement_2(self):
        """if statement"""
        input = """
            class Stmt {
                string temp;
                int call() {
                    int a, c, b, d, e, f, g;
                    if (a == b * c / g && \"8\\b.as\\\"\")[9] then
                        if c then
                            if ((d)) then {
                                x[00] := vanilla_python + false ^ \"\" ^ !nil;
                                return -9e-09 ^ !+{\"?\" , \"str\"};
                            }
                            else {
                                var x = 0;
                                x := y.x();
                            }
                        else
                            io.idle();
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(Id("a"), IntType()),
                                        VarDecl(Id("c"), IntType()),
                                        VarDecl(Id("b"), IntType()),
                                        VarDecl(Id("d"), IntType()),
                                        VarDecl(Id("e"), IntType()),
                                        VarDecl(Id("f"), IntType()),
                                        VarDecl(Id("g"), IntType()),
                                    ],
                                    [
                                        If(
                                            ArrayCell(
                                                BinaryOp(
                                                    "==",
                                                    Id("a"),
                                                    BinaryOp(
                                                        "&&",
                                                        BinaryOp(
                                                            "/",
                                                            BinaryOp(
                                                                "*", Id("b"), Id("c")
                                                            ),
                                                            Id("g"),
                                                        ),
                                                        StringLiteral('"8\\b.as\\""'),
                                                    ),
                                                ),
                                                IntLiteral(9),
                                            ),
                                            If(
                                                Id("c"),
                                                If(
                                                    Id("d"),
                                                    Block(
                                                        [],
                                                        [
                                                            Assign(
                                                                ArrayCell(
                                                                    Id("x"),
                                                                    IntLiteral(0),
                                                                ),
                                                                BinaryOp(
                                                                    "+",
                                                                    Id(
                                                                        "vanilla_python"
                                                                    ),
                                                                    BinaryOp(
                                                                        "^",
                                                                        BinaryOp(
                                                                            "^",
                                                                            BooleanLiteral(
                                                                                False
                                                                            ),
                                                                            StringLiteral(
                                                                                '""'
                                                                            ),
                                                                        ),
                                                                        UnaryOp(
                                                                            "!",
                                                                            NullLiteral(),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                            Return(
                                                                BinaryOp(
                                                                    "^",
                                                                    UnaryOp(
                                                                        "-",
                                                                        FloatLiteral(
                                                                            9e-09
                                                                        ),
                                                                    ),
                                                                    UnaryOp(
                                                                        "!",
                                                                        UnaryOp(
                                                                            "+",
                                                                            ArrayLiteral(
                                                                                [
                                                                                    StringLiteral(
                                                                                        '"?"'
                                                                                    ),
                                                                                    StringLiteral(
                                                                                        '"str"'
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                        ),
                                                                    ),
                                                                )
                                                            ),
                                                        ],
                                                    ),
                                                    Block(
                                                        [
                                                            VarDecl(
                                                                Id("x"),
                                                                ClassType(Id("var")),
                                                                IntLiteral(0),
                                                            )
                                                        ],
                                                        [
                                                            Assign(
                                                                Id("x"),
                                                                CallExpr(
                                                                    Id("y"), Id("x"), []
                                                                ),
                                                            )
                                                        ],
                                                    ),
                                                ),
                                                CallStmt(Id("io"), Id("idle"), []),
                                            ),
                                        )
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_for_statement_1(self):
        """for statement"""
        input = """
            class Stmt {
                int call() {
                    float[10][20] e, f, g, h, i, j;
                    for i := 100 to !+-1 do
                        var := none;
                    d := 1;
                    for something := !(1 == +-\"9\") downto (\"false\") do {
                        DEF obj = a.b.c() + 88.050 ^ 7;
                        if (x) then
                            p.q();
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("e"),
                                            ArrayType(20, ArrayType(10, FloatType())),
                                        ),
                                        VarDecl(
                                            Id("f"),
                                            ArrayType(20, ArrayType(10, FloatType())),
                                        ),
                                        VarDecl(
                                            Id("g"),
                                            ArrayType(20, ArrayType(10, FloatType())),
                                        ),
                                        VarDecl(
                                            Id("h"),
                                            ArrayType(20, ArrayType(10, FloatType())),
                                        ),
                                        VarDecl(
                                            Id("i"),
                                            ArrayType(20, ArrayType(10, FloatType())),
                                        ),
                                        VarDecl(
                                            Id("j"),
                                            ArrayType(20, ArrayType(10, FloatType())),
                                        ),
                                    ],
                                    [
                                        For(
                                            Id("i"),
                                            IntLiteral(100),
                                            UnaryOp(
                                                "!",
                                                UnaryOp(
                                                    "+", UnaryOp("-", IntLiteral(1))
                                                ),
                                            ),
                                            True,
                                            Assign(Id("var"), Id("none")),
                                        ),
                                        Assign(Id("d"), IntLiteral(1)),
                                        For(
                                            Id("something"),
                                            UnaryOp(
                                                "!",
                                                BinaryOp(
                                                    "==",
                                                    IntLiteral(1),
                                                    UnaryOp(
                                                        "+",
                                                        UnaryOp(
                                                            "-", StringLiteral('"9"')
                                                        ),
                                                    ),
                                                ),
                                            ),
                                            StringLiteral('"false"'),
                                            False,
                                            Block(
                                                [
                                                    VarDecl(
                                                        Id("obj"),
                                                        ClassType(Id("DEF")),
                                                        BinaryOp(
                                                            "+",
                                                            CallExpr(
                                                                FieldAccess(
                                                                    Id("a"), Id("b")
                                                                ),
                                                                Id("c"),
                                                                [],
                                                            ),
                                                            BinaryOp(
                                                                "^",
                                                                FloatLiteral(88.05),
                                                                IntLiteral(7),
                                                            ),
                                                        ),
                                                    )
                                                ],
                                                [
                                                    If(
                                                        Id("x"),
                                                        CallStmt(Id("p"), Id("q"), []),
                                                    )
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_for_statement_2(self):
        """for statement"""
        input = """
            class Stmt {
                int main() {
                    bool temp;
                    for _x_ := ((t.y().a != !7--9)) to exp do
                        for y := 2 downto exp1 do {
                            return 1;
                        }
                    for a := this downto nil do {
                        float y = 9;
                        for b := hull[9] to exp2 do
                            return 2;
                        return h.g();
                    }
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("main"),
                                [],
                                IntType(),
                                Block(
                                    [VarDecl(Id("temp"), ClassType(Id("bool")))],
                                    [
                                        For(
                                            Id("_x_"),
                                            BinaryOp(
                                                "!=",
                                                FieldAccess(
                                                    CallExpr(Id("t"), Id("y"), []),
                                                    Id("a"),
                                                ),
                                                BinaryOp(
                                                    "-",
                                                    UnaryOp("!", IntLiteral(7)),
                                                    UnaryOp("-", IntLiteral(9)),
                                                ),
                                            ),
                                            Id("exp"),
                                            True,
                                            For(
                                                Id("y"),
                                                IntLiteral(2),
                                                Id("exp1"),
                                                False,
                                                Block([], [Return(IntLiteral(1))]),
                                            ),
                                        ),
                                        For(
                                            Id("a"),
                                            SelfLiteral(),
                                            NullLiteral(),
                                            False,
                                            Block(
                                                [
                                                    VarDecl(
                                                        Id("y"),
                                                        FloatType(),
                                                        IntLiteral(9),
                                                    )
                                                ],
                                                [
                                                    For(
                                                        Id("b"),
                                                        ArrayCell(
                                                            Id("hull"), IntLiteral(9)
                                                        ),
                                                        Id("exp2"),
                                                        True,
                                                        Return(IntLiteral(2)),
                                                    ),
                                                    Return(
                                                        CallExpr(Id("h"), Id("g"), [])
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_break_statement_1(self):
        """line scopes, for only"""
        input = """
            class Stmt {
                string temp;
                int call() {
                    var hehe;
                    for j := k / j \\ o to {\"17234\", false} do
                        break;
                    for k := a[0] downto (a[10]).y(10) do
                        if k ^ exp then
                            break;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [VarDecl(Id("hehe"), ClassType(Id("var")))],
                                    [
                                        For(
                                            Id("j"),
                                            BinaryOp(
                                                "\\",
                                                BinaryOp("/", Id("k"), Id("j")),
                                                Id("o"),
                                            ),
                                            ArrayLiteral(
                                                [
                                                    StringLiteral('"17234"'),
                                                    BooleanLiteral(False),
                                                ]
                                            ),
                                            True,
                                            Break(),
                                        ),
                                        For(
                                            Id("k"),
                                            ArrayCell(Id("a"), IntLiteral(0)),
                                            CallExpr(
                                                ArrayCell(Id("a"), IntLiteral(10)),
                                                Id("y"),
                                                [IntLiteral(10)],
                                            ),
                                            False,
                                            If(
                                                BinaryOp("^", Id("k"), Id("exp")),
                                                Break(),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_break_statement_2(self):
        """line & block scopes, if & for"""
        input = """
            class Stmt {
                string temp;
                int call() {
                    break;
                    break;
                    if True then {
                        break;
                        if false then break;
                        for obj:= new B() downto new C() do
                            break;
                        break;
                    }
                    break;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        Break(),
                                        Break(),
                                        If(
                                            Id("True"),
                                            Block(
                                                [],
                                                [
                                                    Break(),
                                                    If(BooleanLiteral(False), Break()),
                                                    For(
                                                        Id("obj"),
                                                        NewExpr(Id("B"), []),
                                                        NewExpr(Id("C"), []),
                                                        False,
                                                        Break(),
                                                    ),
                                                    Break(),
                                                ],
                                            ),
                                        ),
                                        Break(),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_continue_statement_1(self):
        """line scopes, for only"""
        input = """
            class Stmt {
                int call() {
                    for Obj := top to b || exp1.a().b > c do
                        if k ^ exp then
                            continue;
                    for var := exp1.a() downto trunc + 99--9  do
                        continue;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        For(
                                            Id("Obj"),
                                            Id("top"),
                                            BinaryOp(
                                                ">",
                                                BinaryOp(
                                                    "||",
                                                    Id("b"),
                                                    FieldAccess(
                                                        CallExpr(
                                                            Id("exp1"), Id("a"), []
                                                        ),
                                                        Id("b"),
                                                    ),
                                                ),
                                                Id("c"),
                                            ),
                                            True,
                                            If(
                                                BinaryOp("^", Id("k"), Id("exp")),
                                                Continue(),
                                            ),
                                        ),
                                        For(
                                            Id("var"),
                                            CallExpr(Id("exp1"), Id("a"), []),
                                            BinaryOp(
                                                "-",
                                                BinaryOp(
                                                    "+", Id("trunc"), IntLiteral(99)
                                                ),
                                                UnaryOp("-", IntLiteral(9)),
                                            ),
                                            False,
                                            Continue(),
                                        ),
                                    ],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_continue_statement_2(self):
        """line & block scopes, if & for"""
        input = """
            class Stmt {
                int call() {
                    var hehe;
                    continue;
                    if a then {
                        continue;
                        for b := c downto d do
                            if e then continue;
                    }
                    continue;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [VarDecl(Id("hehe"), ClassType(Id("var")))],
                                    [
                                        Continue(),
                                        If(
                                            Id("a"),
                                            Block(
                                                [],
                                                [
                                                    Continue(),
                                                    For(
                                                        Id("b"),
                                                        Id("c"),
                                                        Id("d"),
                                                        False,
                                                        If(Id("e"), Continue()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                ),
                            )
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_return_statement_1(self):
        """variables"""
        input = """
            class Stmt {
                string temp;
                int call() {
                    return something;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block([], [Return(Id("something"))]),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_return_statement_2(self):
        """expression"""
        input = """
            class Stmt {
                string temp;
                int call() {
                    return 1 + 2 * \"5\" / !77 \\ 54.8 ^ !-+{\"hehe\"} ^ this.y[9] ^ new A(new B()) % +false - 8 + nil;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        Return(
                                            BinaryOp(
                                                "+",
                                                BinaryOp(
                                                    "-",
                                                    BinaryOp(
                                                        "+",
                                                        IntLiteral(1),
                                                        BinaryOp(
                                                            "%",
                                                            BinaryOp(
                                                                "\\",
                                                                BinaryOp(
                                                                    "/",
                                                                    BinaryOp(
                                                                        "*",
                                                                        IntLiteral(2),
                                                                        StringLiteral(
                                                                            '"5"'
                                                                        ),
                                                                    ),
                                                                    UnaryOp(
                                                                        "!",
                                                                        IntLiteral(77),
                                                                    ),
                                                                ),
                                                                BinaryOp(
                                                                    "^",
                                                                    BinaryOp(
                                                                        "^",
                                                                        BinaryOp(
                                                                            "^",
                                                                            FloatLiteral(
                                                                                54.8
                                                                            ),
                                                                            UnaryOp(
                                                                                "!",
                                                                                UnaryOp(
                                                                                    "-",
                                                                                    UnaryOp(
                                                                                        "+",
                                                                                        ArrayLiteral(
                                                                                            [
                                                                                                StringLiteral(
                                                                                                    '"hehe"'
                                                                                                )
                                                                                            ]
                                                                                        ),
                                                                                    ),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                        ArrayCell(
                                                                            FieldAccess(
                                                                                SelfLiteral(),
                                                                                Id("y"),
                                                                            ),
                                                                            IntLiteral(
                                                                                9
                                                                            ),
                                                                        ),
                                                                    ),
                                                                    NewExpr(
                                                                        Id("A"),
                                                                        [
                                                                            NewExpr(
                                                                                Id("B"),
                                                                                [],
                                                                            )
                                                                        ],
                                                                    ),
                                                                ),
                                                            ),
                                                            UnaryOp(
                                                                "+",
                                                                BooleanLiteral(False),
                                                            ),
                                                        ),
                                                    ),
                                                    IntLiteral(8),
                                                ),
                                                NullLiteral(),
                                            )
                                        )
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_return_statement_3(self):
        """return statement"""
        input = """
            class Stmt {
                string temp;
                int call() {
                    if fatal then
                        return ((!(54.9 * new C(00)) <= -(2)[10])[9]).value;
                    else
                        for i := 10 downto 100 do
                            return io.exit(1);
                    return a.b(0).d.f();
                    return end[00];
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        If(
                                            Id("fatal"),
                                            Return(
                                                FieldAccess(
                                                    ArrayCell(
                                                        BinaryOp(
                                                            "<=",
                                                            UnaryOp(
                                                                "!",
                                                                BinaryOp(
                                                                    "*",
                                                                    FloatLiteral(54.9),
                                                                    NewExpr(
                                                                        Id("C"),
                                                                        [IntLiteral(0)],
                                                                    ),
                                                                ),
                                                            ),
                                                            UnaryOp(
                                                                "-",
                                                                ArrayCell(
                                                                    IntLiteral(2),
                                                                    IntLiteral(10),
                                                                ),
                                                            ),
                                                        ),
                                                        IntLiteral(9),
                                                    ),
                                                    Id("value"),
                                                )
                                            ),
                                            For(
                                                Id("i"),
                                                IntLiteral(10),
                                                IntLiteral(100),
                                                False,
                                                Return(
                                                    CallExpr(
                                                        Id("io"),
                                                        Id("exit"),
                                                        [IntLiteral(1)],
                                                    )
                                                ),
                                            ),
                                        ),
                                        Return(
                                            CallExpr(
                                                FieldAccess(
                                                    CallExpr(
                                                        Id("a"),
                                                        Id("b"),
                                                        [IntLiteral(0)],
                                                    ),
                                                    Id("d"),
                                                ),
                                                Id("f"),
                                                [],
                                            )
                                        ),
                                        Return(ArrayCell(Id("end"), IntLiteral(0))),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_method_invocation_statement_1(self):
        """method invocation statement"""
        input = """
            class Stmt {
                string temp;
                int call() {
                    (8 == new G(\"str{}\", true)).b(param1, \"param2\" && 9);
                    hello.my().world();
                    new hehe().value();
                    (555.9 + 5 - t == Fatal[1]).u(!0 + +9 * false);
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        CallStmt(
                                            BinaryOp(
                                                "==",
                                                IntLiteral(8),
                                                NewExpr(
                                                    Id("G"),
                                                    [
                                                        StringLiteral('"str{}"'),
                                                        BooleanLiteral(True),
                                                    ],
                                                ),
                                            ),
                                            Id("b"),
                                            [
                                                Id("param1"),
                                                BinaryOp(
                                                    "&&",
                                                    StringLiteral('"param2"'),
                                                    IntLiteral(9),
                                                ),
                                            ],
                                        ),
                                        CallStmt(
                                            CallExpr(Id("hello"), Id("my"), []),
                                            Id("world"),
                                            [],
                                        ),
                                        CallStmt(
                                            NewExpr(Id("hehe"), []), Id("value"), []
                                        ),
                                        CallStmt(
                                            BinaryOp(
                                                "==",
                                                BinaryOp(
                                                    "-",
                                                    BinaryOp(
                                                        "+",
                                                        FloatLiteral(555.9),
                                                        IntLiteral(5),
                                                    ),
                                                    Id("t"),
                                                ),
                                                ArrayCell(Id("Fatal"), IntLiteral(1)),
                                            ),
                                            Id("u"),
                                            [
                                                BinaryOp(
                                                    "+",
                                                    UnaryOp("!", IntLiteral(0)),
                                                    BinaryOp(
                                                        "*",
                                                        UnaryOp("+", IntLiteral(9)),
                                                        BooleanLiteral(False),
                                                    ),
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_method_invocation_statement_2(self):
        """static invocation statement"""
        input = """
            class Stmt {
                string temp;
                int call() {
                    a.b(new B(), nil);
                    c.d.e(88 ^ UwU || 0 == true);
                    f.g.h.i(j.k.l(), 999 != 099e-9, {0});
                    1..o(this);
                    this.p(nil.q());
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Stmt"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        CallStmt(
                                            Id("a"),
                                            Id("b"),
                                            [NewExpr(Id("B"), []), NullLiteral()],
                                        ),
                                        CallStmt(
                                            FieldAccess(Id("c"), Id("d")),
                                            Id("e"),
                                            [
                                                BinaryOp(
                                                    "==",
                                                    BinaryOp(
                                                        "||",
                                                        BinaryOp(
                                                            "^",
                                                            IntLiteral(88),
                                                            Id("UwU"),
                                                        ),
                                                        IntLiteral(0),
                                                    ),
                                                    BooleanLiteral(True),
                                                )
                                            ],
                                        ),
                                        CallStmt(
                                            FieldAccess(
                                                FieldAccess(Id("f"), Id("g")), Id("h")
                                            ),
                                            Id("i"),
                                            [
                                                CallExpr(
                                                    FieldAccess(Id("j"), Id("k")),
                                                    Id("l"),
                                                    [],
                                                ),
                                                BinaryOp(
                                                    "!=",
                                                    IntLiteral(999),
                                                    FloatLiteral(9.9e-08),
                                                ),
                                                ArrayLiteral([IntLiteral(0)]),
                                            ],
                                        ),
                                        CallStmt(
                                            FloatLiteral(1.0), Id("o"), [SelfLiteral()]
                                        ),
                                        CallStmt(
                                            SelfLiteral(),
                                            Id("p"),
                                            [CallExpr(NullLiteral(), Id("q"), [])],
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_all_statements_1(self):
        """mixed statements"""
        input = """
            class Mixed {
                string temp;
                static inittt() {
                    local [90] a, b, temp1 = 0.0, temp2;
                    string temp3;
                    if a != +-(!\"$^!@\" % new G().method () + true^(false)) then {
                        break;
                    }
                    else for Int := ((!-new B().haha[0] >= 2 % false ^ 6 ^ \"\\\":\"[6] * 8.e+0[9]) < (!--+{0.23, 3e3})) to (a + (new b()[1] ^ (5 || 7) && !(1 == 6))[\"8\" % false]) do
                        return ((yeh.yoh()[1])[1 + \"string\"]).i[1];
                    continue;
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Mixed"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Static(),
                                Id("<init>"),
                                [],
                                None,
                                Block(
                                    [
                                        VarDecl(
                                            Id("a"),
                                            ArrayType(90, ClassType(Id("local"))),
                                        ),
                                        VarDecl(
                                            Id("b"),
                                            ArrayType(90, ClassType(Id("local"))),
                                        ),
                                        VarDecl(
                                            Id("temp1"),
                                            ArrayType(90, ClassType(Id("local"))),
                                            FloatLiteral(0.0),
                                        ),
                                        VarDecl(
                                            Id("temp2"),
                                            ArrayType(90, ClassType(Id("local"))),
                                        ),
                                        VarDecl(Id("temp3"), StringType()),
                                    ],
                                    [
                                        If(
                                            BinaryOp(
                                                "!=",
                                                Id("a"),
                                                UnaryOp(
                                                    "+",
                                                    UnaryOp(
                                                        "-",
                                                        BinaryOp(
                                                            "+",
                                                            BinaryOp(
                                                                "%",
                                                                UnaryOp(
                                                                    "!",
                                                                    StringLiteral(
                                                                        '"$^!@"'
                                                                    ),
                                                                ),
                                                                CallExpr(
                                                                    NewExpr(
                                                                        Id("G"), []
                                                                    ),
                                                                    Id("method"),
                                                                    [],
                                                                ),
                                                            ),
                                                            BinaryOp(
                                                                "^",
                                                                BooleanLiteral(True),
                                                                BooleanLiteral(False),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                            Block([], [Break()]),
                                            For(
                                                Id("Int"),
                                                BinaryOp(
                                                    "<",
                                                    BinaryOp(
                                                        ">=",
                                                        UnaryOp(
                                                            "!",
                                                            UnaryOp(
                                                                "-",
                                                                ArrayCell(
                                                                    FieldAccess(
                                                                        NewExpr(
                                                                            Id("B"), []
                                                                        ),
                                                                        Id("haha"),
                                                                    ),
                                                                    IntLiteral(0),
                                                                ),
                                                            ),
                                                        ),
                                                        BinaryOp(
                                                            "*",
                                                            BinaryOp(
                                                                "%",
                                                                IntLiteral(2),
                                                                BinaryOp(
                                                                    "^",
                                                                    BinaryOp(
                                                                        "^",
                                                                        BooleanLiteral(
                                                                            False
                                                                        ),
                                                                        IntLiteral(6),
                                                                    ),
                                                                    ArrayCell(
                                                                        StringLiteral(
                                                                            '"\\":"'
                                                                        ),
                                                                        IntLiteral(6),
                                                                    ),
                                                                ),
                                                            ),
                                                            ArrayCell(
                                                                FloatLiteral(8.0),
                                                                IntLiteral(9),
                                                            ),
                                                        ),
                                                    ),
                                                    UnaryOp(
                                                        "!",
                                                        UnaryOp(
                                                            "-",
                                                            UnaryOp(
                                                                "-",
                                                                UnaryOp(
                                                                    "+",
                                                                    ArrayLiteral(
                                                                        [
                                                                            FloatLiteral(
                                                                                0.23
                                                                            ),
                                                                            FloatLiteral(
                                                                                3000.0
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                                BinaryOp(
                                                    "+",
                                                    Id("a"),
                                                    ArrayCell(
                                                        BinaryOp(
                                                            "&&",
                                                            BinaryOp(
                                                                "^",
                                                                ArrayCell(
                                                                    NewExpr(
                                                                        Id("b"), []
                                                                    ),
                                                                    IntLiteral(1),
                                                                ),
                                                                BinaryOp(
                                                                    "||",
                                                                    IntLiteral(5),
                                                                    IntLiteral(7),
                                                                ),
                                                            ),
                                                            UnaryOp(
                                                                "!",
                                                                BinaryOp(
                                                                    "==",
                                                                    IntLiteral(1),
                                                                    IntLiteral(6),
                                                                ),
                                                            ),
                                                        ),
                                                        BinaryOp(
                                                            "%",
                                                            StringLiteral('"8"'),
                                                            BooleanLiteral(False),
                                                        ),
                                                    ),
                                                ),
                                                True,
                                                Return(
                                                    ArrayCell(
                                                        FieldAccess(
                                                            ArrayCell(
                                                                ArrayCell(
                                                                    CallExpr(
                                                                        Id("yeh"),
                                                                        Id("yoh"),
                                                                        [],
                                                                    ),
                                                                    IntLiteral(1),
                                                                ),
                                                                BinaryOp(
                                                                    "+",
                                                                    IntLiteral(1),
                                                                    StringLiteral(
                                                                        '"string"'
                                                                    ),
                                                                ),
                                                            ),
                                                            Id("i"),
                                                        ),
                                                        IntLiteral(1),
                                                    )
                                                ),
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_all_statements_2(self):
        """mixed statements"""
        input = """
            class Mixed {
                string temp;
                int call() {
                    if a then b.c();
                    if a then {b.c();}
                    if c then for i := 0 downto 10 do for j:=11 to 1000e9 do io.print(\"\\thi!\");
                    for k := 7 && 6 || 9 to {\"hehe\"} do if false then io.print(\"hello\\n\");
                }
            }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Mixed"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [],
                                    [
                                        If(Id("a"), CallStmt(Id("b"), Id("c"), [])),
                                        If(
                                            Id("a"),
                                            Block([], [CallStmt(Id("b"), Id("c"), [])]),
                                        ),
                                        If(
                                            Id("c"),
                                            For(
                                                Id("i"),
                                                IntLiteral(0),
                                                IntLiteral(10),
                                                False,
                                                For(
                                                    Id("j"),
                                                    IntLiteral(11),
                                                    FloatLiteral(1000000000000.0),
                                                    True,
                                                    CallStmt(
                                                        Id("io"),
                                                        Id("print"),
                                                        [StringLiteral('"\\thi!"')],
                                                    ),
                                                ),
                                            ),
                                        ),
                                        For(
                                            Id("k"),
                                            BinaryOp(
                                                "||",
                                                BinaryOp(
                                                    "&&", IntLiteral(7), IntLiteral(6)
                                                ),
                                                IntLiteral(9),
                                            ),
                                            ArrayLiteral([StringLiteral('"hehe"')]),
                                            True,
                                            If(
                                                BooleanLiteral(False),
                                                CallStmt(
                                                    Id("io"),
                                                    Id("print"),
                                                    [StringLiteral('"hello\\n"')],
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_all_statements_3(self):
        """mixed statements"""
        input = """
            class Mixed {
                string temp;
                int call() {
                    final hanh a = 1;
                }
            }
            
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Mixed"),
                        [
                            AttributeDecl(
                                Instance(), VarDecl(Id("temp"), StringType())
                            ),
                            MethodDecl(
                                Instance(),
                                Id("call"),
                                [],
                                IntType(),
                                Block(
                                    [
                                        ConstDecl(
                                            Id("a"),
                                            ClassType(Id("hanh")),
                                            IntLiteral(1),
                                        )
                                    ],
                                    [],
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 393))

    """AGGREGATED TESTCASES"""

    def test_testcase_1(self):
        """meaning"""
        input = """
            class sth {}
        """
        expect = str(Program([ClassDecl(Id("sth"), [])]))
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_testcase_2(self):
        """meaning"""
        input = """
            class sth {}
        """
        expect = str(Program([ClassDecl(Id("sth"), [])]))
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_testcase_3(self):
        """meaning"""
        input = """
            class sth {}
        """
        expect = str(Program([ClassDecl(Id("sth"), [])]))
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_testcase_4(self):
        """meaning"""
        input = """
            class sth {}
        """
        expect = str(Program([ClassDecl(Id("sth"), [])]))
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_testcase_5(self):
        """meaning"""
        input = """
            class sth {}
        """
        expect = str(Program([ClassDecl(Id("sth"), [])]))
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_testcase_6(self):
        """meaning"""
        input = """
            class sth {}
        """
        expect = str(Program([ClassDecl(Id("sth"), [])]))
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_testcase_7(self):
        """meaning"""
        input = """
            class sth {}
        """
        expect = str(Program([ClassDecl(Id("sth"), [])]))
        self.assertTrue(TestAST.test(input, expect, 400))
