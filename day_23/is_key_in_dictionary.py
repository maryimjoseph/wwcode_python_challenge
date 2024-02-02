# Day 23 : Write a program that checks if a key exists in a dictionary

# This script builds a dictionary of key-value pairs,
# taking input for the key and value pairs from the user.
# It then accepts the key to lookup in the dictionary from the user
# and displays if the input key exists in the dictionary or not

def is_key_in_dict(p_dict, p_key):
  if p_dict.get(p_key, -1) == -1:
    return False
  else:
    return True

if __name__ == '__main__':
  v_dict = {}
  v_entry = 1

  # build the dictionary
  while(True):
    v_key = input(f'\nEnter the key for entry# {v_entry} : ')
    v_value = input(f'Enter the value for entry# {v_entry} :')
    v_dict[v_key] = v_value
    v_continue = input('Do you wish to input more entries for the dictionary ? Y/N : ')
    if v_continue != 'Y' and v_continue != 'y':
      break

  v_key_check = input('\nEnter the key to lookup in the dictionry : ')
  
  if is_key_in_dict(v_dict, v_key_check):
    print(f'The key {v_key_check} exists in the dictionary')
    print(v_dict)    
  else:
    print(f'The key {v_key_check} does not exist in the dictionary')
    print(v_dict)
