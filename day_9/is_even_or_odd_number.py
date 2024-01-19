# Day 9 : Write a program to check if a number is even or odd.

# The script accepts an integer value
# and displays whether the input number is an even number 
# or an odd number.

def is_even_or_odd(p_number):
  return 'even' if p_number % 2 == 0 else 'odd'

if __name__ == '__main__':
  while(True):
    try:
      v_number = int(input('Please enter an integer value : '))
      print(f'The number {v_number} is an {is_even_or_odd(v_number)} number')
      break
    except ValueError:
      print('Please enter only an integer value\n')
      continue
