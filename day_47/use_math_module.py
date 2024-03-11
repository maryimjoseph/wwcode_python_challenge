# Day 47 : Create a program that imports the math module and uses its functions

# This script utilizes some of the functions from the math module

import math

def area_of_circle(p_radius):
  return math.pi * pow(p_radius, 2)

if __name__ == '__main__':
  try:
    r = float(input('Enter radius of the cirlce : '))
    print(f'The value of pi is : {math.pi}')
    a = area_of_circle(r)
    print(f'Area of circle is : {a}')

    print(f"Ceiling value of the circle's area is : {math.ceil(a)}")
    print(f"Floor value of the circle's area is : {math.floor(a)}") 

    print(f'Factorial of {int(r)} is : {math.factorial(int(r))}') 
    print(f'GCD of {int(r)} and {int(a)} is : {math.gcd(int(r), int(a))}')

    print(f'Log of 10 base 10 is : {math.log(10, 10)}')
  except ValueError:
    print('Please enter a numeric value for the radius')
