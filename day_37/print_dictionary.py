# Day 37 : Write a program to iterate through a dictionary and print its keys and values

# This script prints the keys and values of a dictionary

def print_dictionary(p_dict):
  for key, val in p_dict.items():
    print(f'{key} : {val}')

if __name__ == '__main__':
  v_dict = {'CA':'California', 'TX':'Texas', 'OH':'Ohio', 'NV':'Nevada'}
  print_dictionary(v_dict)
