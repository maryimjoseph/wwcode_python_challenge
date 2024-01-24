# Day 15 : Write a program to print the first n numbers of a Fibonacci sequence

# This script takes an integer value(n) as input
# and prints the first n numbers of a Fibonacci sequence

def print_fibonacci_series(p_prev_val, p_curr_val, p_count):

  if p_prev_val == 0:
    print(f'{p_prev_val}, {p_curr_val}', end='')    
  else:
    print(f', {p_curr_val}', end='')

  v_sum = p_prev_val + p_curr_val
  v_prev_val = p_curr_val
  v_curr_val = v_sum

  v_count = p_count - 1
  if v_count > 1 :
    print_fibonacci_series(v_prev_val, v_curr_val, v_count)


if __name__ == '__main__':
  while(True):
    try: 
      v_number = int(input('Please enter a number greater than 0 : '))
      print(v_number)
      if v_number <= 0:
        continue

      print_fibonacci_series(0, 1, v_number)
      break
      
    except ValueError:
      print('Please enter only an integer value\n')
      continue

