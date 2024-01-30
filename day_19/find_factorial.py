# Day 19 : Write a function to calculate the factorial of a number.

# This script uses recursion to find the factorial of a given number.

def find_factorial(p_num):
  if p_num == 1 or p_num == 0:
    return 1
  return p_num * find_factorial(p_num - 1)

if __name__ == '__main__':
  while(True):
    try:
      v_num = int(input('Please enter a number(integer) : '))
      if v_num < 0:
        print('Please enter a non-negative number\n')
        continue
      break
    except ValueError:
      print('Please enter an integer value\n')

  print(f'Factorial of {v_num} is : ', find_factorial(v_num))
