# Day 33 : Write a test case for a function that checks if a number is prime

# Test case for a function that checks if a number is prime

# Prime Number :
# Any whole number which is greater than 1 and has only two factors,
# that is 1 and the number itself, is called a prime number

# Checking if a number is prime using the Trial Division Method,
# where the number is divided by every integer between 2 and the square root
# of the number. If no remainder is left in any of the divisions,
# then the number is prime.

import sys
import math
import unittest

def is_prime_number(v_number):
  if v_number <= 1:
    return False
  for i in range(2, int(math.sqrt(v_number))+1):
    if v_number % i == 0:
      return False
  return True

# Creating a class that inherits from another class
# https://www.pythonmorsels.com/inheriting-one-class-another/
# To create a class that inherits from another class, 
# after the class name you'll put parentheses and then list any classes 
# that your class inherits from.

# In a function definition, parentheses after the function name
# represent arguments that the function accepts. 
# In a class definition the parentheses after the class name instead 
# represent the classes being inherited from.

# Define test case class that inherits from the class, unitest.TestCase
class test_is_prime_number(unittest.TestCase):

  def test_prime_numbers(self):
    v_prime_numbers = [2, 3, 7, 11, 13]      
    for num in v_prime_numbers:
      self.assertTrue(is_prime_number(num), \
        f'The fucntion returns False and identifies {num} a non-prime number')

  def test_non_prime_numbers(self):
    v_non_prime_numbers = [4, 6, 8, 9, 10]
    for num in v_non_prime_numbers:
      self.assertFalse(is_prime_number(num), \
        f'The fucntion returns True and identifies {num} a prime number')

if __name__ == '__main__':
  # print(f'{is_prime_number(17)}')
  # unittest.main()
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
