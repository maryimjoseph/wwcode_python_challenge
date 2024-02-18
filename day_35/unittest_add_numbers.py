# Day 35 : Write a simple unit test for a function that adds two numbers

# This script contains a function to add 2 numbers 
# and test cases to test addition of numeric and non-numeric values.

import unittest

def add_numbers(v_num_1, v_num_2):
    return float(v_num_1 + v_num_2)

class test_case_add_numbers(unittest.TestCase):
  def test_add_numbers(self):
    self.assertEqual(add_numbers(1, 3), 4)
    self.assertEqual(add_numbers(-1, -3), -4)
    self.assertEqual(add_numbers(-1, 1), 0)    

  def test_add_non_numbers(self):
    # self.assertRaises(ValueError, add_numbers, 'a', 'b')
    with self.assertRaises(ValueError):
      v_sum = add_numbers('a', 'b')

if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)  
