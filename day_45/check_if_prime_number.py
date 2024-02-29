# Day 45 : Write a function to check if a number is a prime number

# This script takes an integer input
# and determines if the integer is a prime number

# Prime Number :
# Any whole number which is greater than 1 and has only two factors,
# that is 1 and the number itself, is called a prime number

# Checking if a number is prime using the Trial Division Method,
# where the number is divided by every integer between 2 and the square root
# of the number. If no remainder is left in any of the divisions,
# then the number is prime.

import math

def is_prime(p_number):
  if p_number <= 1:
    return False
  for i in range(2, int(math.sqrt(p_number))+1):
    if p_number % i == 0:
      return False
  return True
      
if __name__ == '__main__':
  while(True):
    try:
      v_number = int(input('Enter an integer value : ' ))
      if is_prime(v_number):
        print(f'{v_number} is a prime number')
      else:
        print(f'{v_number} is not a prime number')
      break
    except ValueError:
      print(f'Enter only an integer value')
