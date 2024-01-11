
# Day 1 : Create a program that swaps the values of two variables.

# This script takes two variable values as input
# and displays the input values for those variables.
#
# It then swaps the content of the those two variables  
# and displays the variables with their swapped values. 

var1 = input('Enter the value of the 1st variable : ')
var2 = input('Enter the value of the 2nd variable : ')

print('\nOriginal values of the variables :')
print('Variable 1 : ', var1)
print('Variable 2 : ', var2)

tmpvar = var1
var1 = var2
var2 = tmpvar

print('\nValues of the variables after the swap :')
print('Variable 1: ', var1)
print('Variable 2: ', var2)



