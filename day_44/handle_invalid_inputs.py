# Day 44 : Write a program that reads an integer from the user and handles invalid inputs

# This script requests for an integer value from the user
# and handles invalid inputs

while(True):
  try:
    v_int_number = int(input('Enter an integer value : '))
    break
  except ValueError:
    print('Enter only an integer value\n')
