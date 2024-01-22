# Write a program to reverse a given string.

# This script takes a string input and 
# prints it in reverse

def reverse_string(p_str):
  return p_str[::-1]

if __name__ == '__main__':
  while(True):
    v_str = input('Please input a string : ')
    if len(v_str) < 2:
      print('Please enter a string value (2 characters or more in length)')
      continue
    else:
      break
  
  v_str_reversed = reverse_string(v_str)
  print(f'The string in reverse is : {v_str_reversed}')
