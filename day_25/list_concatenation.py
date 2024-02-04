# Day 25 : Create a program to concatenate two lists.

# Genereates two lists based on two string inputs with comma delimited values.
# The List#1 is then extended to include to the elements from List2

def concatenate_list(p_list1, p_list2): # Lists are passed by reference
  p_list1.extend(p_list2)

if __name__ == '__main__':
  v_string1 = input('Enter a string of elements separated by commas : ')
  v_list1 = v_string1.split(',')

  v_string2 = input('Enter another string of elements separated by commas : ')
  v_list2 = v_string2.split(',')

  print(f'\nList1 : {v_list1}')
  print(f'List2 : {v_list2}')
  concatenate_list(v_list1, v_list2)

  print(f'\nConcatenated list : {v_list1}')
