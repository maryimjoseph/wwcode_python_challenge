# Day 11 : Write a program to print the multiplication table of a given number

# This script takes an integer input and prints 
# the multiplication table for that integer. 

def print_multiplication_table(p_number):
  for i in range(1, 13):
    v_product = i * p_number;
    print(f'{v_number} * {i} = {v_product}')

if __name__ == '__main__':
  while(True):
    try:      
      v_number = int(input('Enter the number for the multiplication table : '))
      print_multiplication_table(v_number)    
      break
    except ValueError:
      print('Please input an integer value only\n')
