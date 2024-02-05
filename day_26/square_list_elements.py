# Day 26 : Create a program that uses a lambda function to square each element of a list.

# This script takes a list of integers as an input,
# applies a lambda function to square each element of the list
# and displays the resultant list.

def square_elements_in_list(p_list):
  return list(map(lambda x : x ** 2, p_list))

if __name__ == '__main__':
  while(True):
    try:
      v_string_list = input('Enter a list of integers separated by commas : ')
      v_list_integers = [int(i) for i in v_string_list.split(',')]
      break;
    except ValueError:
      print('Please enter only a list of integer values')
      continue

  print 
  v_list_of_squares = square_elements_in_list(v_list_integers)
  print(v_list_of_squares)
