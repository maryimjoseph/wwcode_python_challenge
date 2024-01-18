# Day 8 : Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

# This script takes a string as input and 
# displays the number of uppercase and lowercase characters in the string.

def count_uppercase_lowercase_chars():
  v_count_upper, v_count_lower = 0, 0
  
  while(True):
    v_str = input('Please enter a string of characters : ')
    if len(v_str) > 2:
      break
    else:
      print('Please enter a string longer than 1 character in length')

  # Find the count of uppercase and lowercase characters in the input string
  for i in v_str:
    if i.isupper():
      v_count_upper += 1
    elif i.islower():
      v_count_lower+=1
    
  print(f"The count of uppercase characters in '{v_str}' is {v_count_upper}")
  print(f"The count of lowercase characters in '{v_str}' is {v_count_lower}")

if __name__ == '__main__':
  count_uppercase_lowercase_chars();
