# Day 21 : Create a program to remove a specific element from a set

# This script creates a set of elements based on a string input
# of elements separated by commas. It then takes the value of 
# the element to remove as an input, removes the element from the set
# and displays the updated set.

def remove_from_set(p_set, p_item_to_remove):
  p_set.discard(p_item_to_remove)
  return p_set

if __name__ == '__main__':
  v_set_string = input('Enter a list of elements separated by commas : ')
  v_set = set(i.strip() for i in v_set_string.split(','))

  v_element_to_remove = input('\nEnter the element to remove from the set : ')

  print('\nThe original set of elements was : ', v_set, '\n')
  print('The element to be removed : ', v_element_to_remove, '\n')
  
  v_updated_set = remove_from_set(v_set, v_element_to_remove)  
  print(f'The updated set after removing {v_element_to_remove} is ', v_updated_set)
