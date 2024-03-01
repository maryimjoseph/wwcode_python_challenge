# Day 46 : Write a function to check if a given list is sorted

# This script takes as comma delimited string of integers as input
# and builds a list and checks to see if the elements of the list
# are in sorted order.

def is_list_sorted(p_list):
  v_list_sorted_asc = sorted(v_list)
  v_list_sorted_desc = sorted(v_list, reverse=True)  
  if p_list == v_list_sorted_asc or p_list == v_list_sorted_desc:
    return True
  else:
    return False

if __name__ == '__main__':
  v_string_list = input('Enter a sequence of integers separated by commas : ')
  v_list = list(map(int, v_string_list.split(',')))
  
  if is_list_sorted(v_list):
    print(f'The list {v_list} is sorted')
  else:
    print(f'The list {v_list} is not sorted')    
