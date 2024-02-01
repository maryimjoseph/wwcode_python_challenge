# Day 22 : Create a program to find the second-largest element in a list.

# This script takes in a string of elements separated by commas, as an input and
# returns the 2nd largest element(based on the length of the element),
# as the output.

def find_second_largest_element(p_list):
  v_list_sorted = sorted(p_list, key=lambda x : len(x), reverse=True)
  return v_list_sorted[1]

if __name__ == '__main__':
  v_string = input('Enter a list of values separated by commas : ')
  v_list = [i.strip() for i in v_string.split(',')]
  print(find_second_largest_element(v_list))
  
