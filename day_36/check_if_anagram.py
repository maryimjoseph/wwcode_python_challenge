# Day 36 : Write a Python program to check if two strings are anagrams

# This script takes 2 strings as input and
# checks if those 2 strings are anagrams and displays the result.

# Anagram : a word or phrase made by transposing the letters of another word or phrase.
# The word "secure" is an anagram of "rescue."

def is_anagram(p_string1, p_string2):
  v_list1 = list(p_string1)
  v_list1.sort()

  v_list2 = [ x for x in p_string2]
  v_list2 = sorted(v_list2)

  return v_list1 == v_list2

if __name__ == '__main__':
  while(True):
    v_string1 = input('Enter String#1 : ')
    if len(v_string1.strip()) == 0:
      print('Input a sequence of characters for String#1')
      continue
    else:
      break

  while(True):
    v_string2 = input('Enter String#2 : ')
    if len(v_string2.strip()) == 0:
      print('Input a sequence of characters for String#2')
      continue
    else:
      break

  if is_anagram(v_string1, v_string2):
    print(f"String#1 ('{v_string1}') and String#2 ('{v_string2}') are anagrams")
  else:
    print(f"String#1 ('{v_string1}') and String#2 ('{v_string2}') are not anagrams")
