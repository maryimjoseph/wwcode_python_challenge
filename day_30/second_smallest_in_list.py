# Day 30 : Create a function that finds the second smallest element in a list

# This script takes in a comma separated string of numbers as input
# and prints the 2nd smallest element from the list.

def find_second_smallest_element(p_list_float):
    p_list_float.sort()
    return p_list_float[1]

if __name__ == '__main__':
  while(True):
    try:
      v_list_string = input('Enter a list of elements separated by commas : ')
      v_list_float =  [float(i) for i in v_list_string.split(',')]
      if len(v_list_float) < 2:
        print('\nPlease include more than one elemnet in your input')
        continue
      break
    except ValueError:
      print('\nPlease enter only numeric values separated by commas')

  print(f'You list of elements : {v_list_float} ')
  print(f'Your second smallest element is : {find_second_smallest_element(v_list_float)}')
