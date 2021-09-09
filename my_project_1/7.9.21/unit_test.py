# import unittest
# from calculator.py import calc_1
#
#
# addtwo = lambda x: x + 2
#
# class LambdaTest(unittest.TestCase):
#     def test_add_two(self):
#         self.assertEqual(addtwo(2), 4)
#
#     def test_add_two_point_two(self):
#         self.assertEqual(addtwo(2.2), 4.2)
#
#     def test_add_three(self):
#         # Should fail
#         self.assertEqual(addtwo(3), 5)
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)


# Python program for simple calculator
import unittest
import unittest_functions

class LearnTest(unittest.TestCase):
    def setUp(self):
        self.a = int(input("\nenter first number:"))
        self.b = int(input("\nenter second number:"))
        # self.a = 20
        # self.b = 30
    def testsum(self):
        self.assertEqual(unittest_functions.add(self.a,self.b),self.a+self.b)
    def testsubtract(self):
        self.assertEqual(unittest_functions.subtract(self.a,self.b),self.a-self.b)
    def testmultiply(self):
        self.assertEqual(unittest_functions.multiply(self.a,self.b),self.a*self.b)
    def testdivide(self):
        self.assertEqual(unittest_functions.divide(self.a,self.b),self.a/self.b)


if __name__	=='__main__':
    unittest.main(verbosity=2)


