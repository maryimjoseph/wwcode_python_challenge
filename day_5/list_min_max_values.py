# Day 5 : Write a program to find the maximum and minimum values in a list

# This script takes a comma delimited string as input. 
# It then converts the input it to a list of numbers 
# and displays the minimum and maximum values from the list

def input_list():
  try:
    v_list = list(map(float, input("Enter a list of integers separated by commas :").split(',')))
    return v_list    
  except ValueError :
    print("Error: Please only input numbers, separated by commas.")
    return None  

if __name__ == '__main__':
  v_list_of_numbers = input_list()
  print(v_list_of_numbers)
  min_value = min(v_list_of_numbers)
  max_value = max(v_list_of_numbers)
  print(f'Minimum value is {min_value}\nMaximum value is {max_value}')
