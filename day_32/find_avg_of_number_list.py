# Day 32 : Create a function that calculates the average of a list of numbers

import functools

# This script accepts a string of numbers separated by commas as input
# and prints the average of the list of numbers.

def find_average(p_list):
  v_average = functools.reduce(lambda a, b : a + b, v_list)/len(v_list)
  return v_average

if __name__ == '__main__':
  v_string_list = input('Please input a list of numbers separated by commas : ')
  v_list = [float(i) for i in v_string_list.split(',')]

  print(f'The averaage of the list {v_list} is : ', end="")
  print(find_average(v_list))
