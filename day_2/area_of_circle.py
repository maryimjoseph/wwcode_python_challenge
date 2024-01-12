# Day 2 : Create a program to calculate the area of a circle given its radius.

# Takes the radius of a circle as input,
# computes its area (pi * r ** 2) and displays it.

from math import pi

radius = int(input('Enter the radius of the circle : '))
area_of_circle = pi * radius ** 2
print('The area of the circle is : ', area_of_circle)
