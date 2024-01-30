# Day 18 : Create a program to find the largest among three numbers.

# The script takes an input string of 3 numbers separated by commas
# and prints the largest among the three numbers.

def find_largest_number(p_num_list):
  return max(p_num_list)

if __name__ == '__main__':
 
  while(True):
    try:
      v_string_of_num = input('Enter 3 numbers separated by commas : ')
      v_num_list = [int(i.strip()) for i in v_string_of_num.split(',')]
      if len(v_num_list) != 3:
        continue

      break
    except ValueError:
      print('Please enter only numeric values\n')

  print('The largest number is :', find_largest_number(v_num_list))
