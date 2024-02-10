# Day 31 : Create a program that checks if a given string is a valid email address.

# This script takes an email address as input
# and checks the validity of the email address.
# It displays the reason for considering an email as invalid.

from email_validator import validate_email, EmailNotValidError

v_email = input('Enter an email addreass : ')
try:
  validate_email(v_email)
  print(f"The Email address : '{v_email}' is valid") 
except EmailNotValidError as e:
  print('Invalid email : ', str(e))
