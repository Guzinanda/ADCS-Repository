'''
@ TITLE:    filecmp.py
@ DATE:     25-03-2020
@ AUTHOR:   Fernanda Guzman Gomez
@ PROBLEM:  Exercise 19
'''

import unittest
import filecmp


# UNIT TESTING _____________________________________________

class Testing(unittest.TestCase):

    def test_file_cmp_true(self):
        self.assertEqual(filecmp.cmp('file1.txt', 'file2.txt'), True)

    def test_file_cmp_false(self):
        self.assertEqual(filecmp.cmp('file1.txt', 'file3.txt'), False)


# CODE ____________________________________________________

file1 = 'file1.txt'  # Happy Path (Because True)
file2 = 'file2.txt'

file1 = 'file1.txt'  # Happy Path (Because False)
file3 = 'file3.txt'


if __name__ == '__main__':
    unittest.main()
