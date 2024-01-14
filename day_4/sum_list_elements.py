# Day 4 : Write a program to find the sum of all elements in a list

# This script finds calculates the sum of all elements in a list 
# and displays the sum on the screen.

def sum_of_list_elements(p_list):
  v_sum = 0
  for i in p_list:
    v_sum += i
  return v_sum

if __name__ == '__main__':
  v_list = [10, 20, 30, 40, 50]
  print(f'The Sum of list elements is {sum_of_list_elements(v_list)}')
  
