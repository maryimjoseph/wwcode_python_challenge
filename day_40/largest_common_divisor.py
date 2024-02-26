# Day 40 : Write a function to find the largest common divisor of two numbers using a function

# This script takes in 2 integers as input and 
# prints the largest common divisor for the 2 integers.

def find_largest_common_divisor(p_num1, p_num2):
  v_div_num1_list = []
  v_div_num2_list = []

  for i in range(1, p_num1+1):
    if p_num1 % i == 0:
      v_div_num1_list.append(i)

  for i in range(1, p_num2+1):
    if p_num2 % i == 0:
      v_div_num2_list.append(i)

  v_common_elements = set(v_div_num1_list) & set(v_div_num2_list)
  v_common_divisors_sorted_desc = list(sorted(v_common_elements, reverse=True))
  return v_common_divisors_sorted_desc[0]


if __name__ == '__main__':

  while(True):
    try:
      v_num1 = int(input('Enter an integer value for the 1st number : '))
      break
    except ValueError:
      print('Please enter an integer value')

  while(True):
    try:
      v_num2 = int(input('Enter an integer value for the 2nd number : '))
      break
    except ValueError:
      print('Please enter an integer value')

  v_largest_common_divisor = find_largest_common_divisor(v_num1, v_num2)
  print(f'The Largest Common Divisor of {v_num1} and {v_num2} is {v_largest_common_divisor}')
