# Day 13 : Write a program to shuffle the elements of a list randomly

# This script takes a comma delimited list of values as input
# and shuffles the list elements in random order
 
import random

def shuffle_list_elements(p_list):
  random.shuffle(p_list)
  return p_list

if __name__ == '__main__':
  v_clean_list = []
  v_string = input('Input a list of values separated by commas : ')

  for i in v_string.split(','):
    v_clean_list.append(str(i).strip())
  print(f'Original list(trimmed) is : {v_clean_list}')

  v_list_shuffled = shuffle_list_elements(v_clean_list)
  print(f'Shuffled list : {v_list_shuffled}')
