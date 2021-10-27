import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_00(self):
        input = """class main {}
        class main {}"""
        expect = "Redeclared Class: main"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_01(self):
        input = """class main {
            int a, a;
        }"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_02(self):
        input = """class main {
            void a() {}
            int a() {}
        }"""
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_03(self):
        input = """class main {
            static int a;
            static int a;
        }"""
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_04(self):
        input = """class main {
            void a () {
                int a;
                int a;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_05(self):
        input = """class main {
            static A t;
            static void x () {
                int a;
            }
        }
        class abc {
            abc x;
        }
        """
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_06(self):
        input = """class main {
            final int a = 1.0 % 2;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,FloatLit(1.0),IntLit(2))"
        self.assertTrue(TestChecker.test(input,expect,406))
    
    def test_07(self):
        input = """class main {
            int a () {
                int t;
                t := 0.5;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(t),FloatLit(0.5))"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_08(self):
        input = """class main {
            int t;
            int a () {
                t := 1.0 + 2;
            }
        }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(t),BinaryOp(+,FloatLit(1.0),IntLit(2)))"
        self.assertTrue(TestChecker.test(input,expect,408))