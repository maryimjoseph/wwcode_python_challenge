# Day 2 : Create a program to calculate the area of a circle given its radius.

# Takes the radius of a circle as input,
# computes its area (pi * r ** 2) and displays it.

from math import pi

def input_circle_radius():
  try:
    r = float(input('Enter the radius of the circle : '))
    return r
  except ValueError:
    print('Please type in a numeric value for the radius')
    return -1

radius = input_circle_radius()

if radius != -1:
  area_of_circle = pi * radius ** 2
  print('The area of the circle is : ', area_of_circle)
