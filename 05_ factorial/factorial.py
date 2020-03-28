'''
@ TITLE:    factorial.py
@ DATE:     25-03-2020
@ AUTHOR:   Fernanda Guzman Gomez
@ PROBLEM:  Exercise 17
'''

import unittest
import math


# UNIT TESTING _____________________________________________

class Testing(unittest.TestCase):
    """ 
    This is a class test cases. 
      
    Attributes: 
        self (the type of the class): ...

    """
    
    def test_factorial_a(self):
        self.assertEqual(math.factorial(1), 1)

    def test_factorial_b(self):
        self.assertEqual(math.factorial(6), 720)

    def test_factorial_c(self):
        with self.assertRaises(ValueError): math.factorial(2.5)

    def test_factorial_d(self):
        with self.assertRaises(ValueError): math.factorial(-1)

    def test_factorial_d(self):
        with self.assertRaises(TypeError):
            math.factorial('a')


# CODE ____________________________________________________     

a = 1       # Happy Path
b = 6       # Happy Path
c = 2.5     # Edge Case
d = -1      # Edge Case
e = 'a'     # Sad Path

# print("factorial of", a, "is = ", math.factorial(a))
# print("factorial of", b, "is = ", math.factorial(b))
# print("factorial of", c, "is = ", math.factorial(c))
# print("factorial of", d, "is = ", math.factorial(d))
# print("factorial of", e, "is = ", math.factorial(e))


if __name__ == '__main__':
    unittest.main()
