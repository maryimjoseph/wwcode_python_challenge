# Day 42 : Write a program that uses a try-except block to handle division by zero

# This script uses a try-except block to handle division by zero

while(True):
  try:
    v_numerator = int(input('Enter an integer value for the numerator : '))
    v_denominator = int(input('Enter an integer value for the denominator :'))
    v_result = int(v_numerator / v_denominator)
    break
  except ZeroDivisionError:
    print('Zero Division Error : Cannot divide a number by zero\n')
    continue
print(f'The result is : {v_result}')
