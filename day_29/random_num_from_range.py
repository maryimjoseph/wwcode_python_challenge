# Day 29 : Create a function that generates a random number between a given range.

# This script takes the lower and upper limits as inputs to denote a number range
# and displays a random number from this range.

from random import randint

def random_num_from_range(p_low_limit, p_upper_limit):
  return randint(p_low_limit, p_upper_limit)

if __name__ == '__main__':
  while(True):
    try:
      print('Random Number Generator based on a given range\n')
      v_low_limit = int(input('Enter an integer denoting the lower limit : '))
      v_upper_limit = int(input('Enter an integer denoting the upper limit : ')) 
      if v_low_limit > v_upper_limit:
        print('Invalid entries : The lower limit should be lesser than the upper limit')
        continue
      break
    except ValueError:
      print('\nPlease enter only integer values')
      continue
    
  print(f'Here is a random number between your range of {v_low_limit} and {v_upper_limit} : \
{random_num_from_range(v_low_limit, v_upper_limit)}')
