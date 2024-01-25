# Day 15: Create a program that checks if a year is a leap year.

# How to determine if a year is a Leap year
# https://www.wikihow.com/Calculate-Leap-Years
# If a year is evenly divisible by 4, 
# but it is not evenly divisible 100, then it is a leap year.

# If a year is divisible by both 4 and 100, 
# then it might not be a leap year,
# you will have to perform 1 more calculation to check.

# If a year is divisible by 100, but not 400, then it is not a leap year. 
# If a year is divisible by both 100 and 400, then it is a leap year.

def is_leap_year(p_year):
  if (p_year % 4 == 0 and p_year % 100 !=0) \
    or (p_year % 4 == 0 and p_year % 100 == 0 and p_year % 400 == 0):
    return True
  else:
    return False

if __name__ == '__main__':
  while(True):
    v_year = input('Enter a 4 digit year : ')
    if len(v_year.strip()) != 4:
      print('Please input a 4 digit year\n')
      continue
    else:
      if is_leap_year(int(v_year.strip())):
        print(f'{v_year.strip()} is a leap year')
      else:
        print(f'{v_year.strip()} is not a leap year')        
      break  
  
