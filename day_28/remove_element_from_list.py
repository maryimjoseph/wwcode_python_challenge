# Day 28 : Create a program that removes the nth element from a list.

# This script creates a list, based on a string input of a sequence of elements.
# It then takes an input for the element number to be removed from the list
# and removes that element.

def remove_list_element(p_list, p_element_num):
  p_list.pop(p_element_num-1)
  return p_list

if __name__ == '__main__':
  v_list_string = input('Enter a list of elements separated by commas : ')
  v_list = v_list_string.split(',')
  print('The list is : ', v_list)

  while(True):
    try:
      v_element_num = \
        int(input('Enter the element you wish to remove from the list : '))
      if v_element_num > len(v_list):
        print(f'\nThe length of the list is : {len(v_list)}')
        print(f'Enter an element number between 1 and {len(v_list)}')
      else:
        break
    except ValueError:
      print('\nPlease enter a numeric value for the element to be removed')
      continue

  print(f'\nThe updated list after removing element# {v_element_num} is :\n \
{remove_list_element(v_list, v_element_num)}')
