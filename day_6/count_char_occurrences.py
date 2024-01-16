# Day 6 : Write a program to count the occurrences of a specific character in a string

# This script inputs a string value and the character for which the count 
# of occurences is expected to be found. It loops through the string input value 
# to find the count of the characters and displays it on the screen.

def count_char_occurences(p_str, p_char):
  v_count_char = 0
  for i in p_str:
    if i == p_char:
      v_count_char += 1
  return v_count_char;

if __name__ == '__main__':
  v_str = input('Enter a string : ')
  v_char = input('The character to look for in the string : ')
  v_cnt_char = count_char_occurences(v_str, v_char)
  print(f'There were' if v_cnt_char > 1 else 'There is', v_cnt_char, 
    'occurences of' if v_cnt_char > 1 else 'occurance of', '\''+v_char+'\'', 'in', '\''+v_str+'\'')
