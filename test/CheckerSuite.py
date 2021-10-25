import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # def test_00(self):
    #     input = """class main {}
    #     class main {}"""
    #     expect = "Redeclared Class: main"
    #     self.assertTrue(TestChecker.test(input, expect, 400))

    # def test_01(self):
    #     input = """class main {
    #         int a, a;
    #     }"""
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_02(self):
    #     input = """class main {
    #         void a() {}
    #         int a() {}
    #     }"""
    #     expect = "Redeclared Method: a"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_03(self):
    #     input = """class main {
    #         static int a;
    #         static int a;
    #     }"""
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,403))

    # def test_04(self):
    #     input = """class main {
    #         void a () {
    #             int a;
    #             int a;
    #         }
    #     }
    #     """
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,404))

    def test_05(self):
        input = """class main {
            void a () {
                int b;
                int a = b + 5;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,405))
    
