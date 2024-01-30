# Day 20 : Write a function that takes a list of numbers and returns a new list containing only the even numbers.

# This script takes a list of integers as input 
# and prints the list of even numbers

def return_even_numbers(p_num_list):
  v_list_even_num = []  
  for i in p_num_list:
    if i % 2 == 0:
      v_list_even_num.append(i)
  return v_list_even_num

if __name__ == '__main__':
  while(True):
    try:
      v_string_of_num = input('Enter a list of integers separated by commas : ')
      v_num_list = [int(i.strip()) for i in v_string_of_num.split(',')]
      break
    except ValueError:
      print('Please enter only integer values separated by commas\n')
      continue

  print('List of even numbers :', return_even_numbers(v_num_list))
