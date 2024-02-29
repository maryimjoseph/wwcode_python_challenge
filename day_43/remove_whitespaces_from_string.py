# Day 43 : Write a program that removes all whitespaces from a given string

# This script takes a string as input and 
# removes all whitespaces from the string

import re

def remove_whitespaces(p_string):
  # return p_string.replace(' ', '')
  string_wo_whitespaces = re.sub(r'\s+', '', p_string)
  return string_wo_whitespaces 
  
if __name__ == '__main__':
  v_string = input('Enter a string with spaces and/or tabs : ')
  v_string_stripped = remove_whitespaces(v_string)
  print(f'The string without whitespaces : {v_string_stripped}')
