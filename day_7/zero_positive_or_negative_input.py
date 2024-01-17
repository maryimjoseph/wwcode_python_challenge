# Day 7 : Write a program to check if a number is positive, negative or zero

# The script takes in a numeric input and
# and displays if the input number is positive 
# or a negative number or a zero.

if __name__ == '__main__':
  while(True):
    try:
      v_number = float(input('Please enter a number :'))
      exit
    except ValueError:
      print('Please enter a numeric value only')
      continue

    if v_number == 0:
      print('The number is zero')
    elif v_number > 0:
      print('The number is positive')
    else:
      print('The number is negative')
