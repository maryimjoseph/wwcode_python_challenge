# Day 24 : Write a program to remove vowels from a given string.

# This script takes in a string input, removes the vowels from the string
# and displays the string with the vowels removed.

import re
  
def remove_vowels(p_string):
  return re.sub('[aeiouAEIOU]', '', p_string)

if __name__ == '__main__':
  v_string = input('Please input a string : ')
  v_updated_string = remove_vowels(v_string)
  print(f"The original string is : '{v_string}'")
  print(f"The string with the vowels removed is : '{v_updated_string}'")
