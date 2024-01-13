# Day 3 : Write a function to count the number of vowels in a given string

# This script takes a string as input and 
# prints the number of vowels in the input string.

def count_vowels(textvalue):
  vowels_list = ['a', 'e', 'i', 'o', 'u']
  vowel_count = 0
  for i in range(0, len(textvalue)):
    if textvalue[i] in vowels_list: 
      vowel_count += 1
  return vowel_count

if __name__ == '__main__':
  input_string = input("Enter a string value : ")
  lowercase_input_string = input_string.lower()
  print(f'The number of vowels in {input_string} is {count_vowels(lowercase_input_string)}')
