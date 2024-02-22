# Day 38 : Write a program to flatten a nested list

# Python | Convert a nested list into a flat list
# https://www.geeksforgeeks.org/python-convert-a-nested-list-into-a-flat-list/?ref=lbp
# Using recursion 

# This script flattens a nested list and
# prints the flattened list

def flatten_list(p_list):
  flat_list = []
  
  for element in p_list:
    if type(element) is list:
      flat_list.extend(flatten_list(element))
    else:
      flat_list.append(element)
  return flat_list

if __name__ == '__main__':
  v_list =  [[11, 22, 33, 44], [55, 66, 77], [88, 99, [1,2]]]
  print(flatten_list(v_list))
