# Day 54 : Create a function to find all words in a sentence that start with a vowel

# Takes a sentence as an input and lists the words from the sentence 
# which begin with a vowel.

import re

def words_beginning_with_vowel(p_list):
  sentence_list = p_list.lower().split(' ')  
  words_begin_with_vowel = list(filter(lambda x: x[0] in ['a', 'e', 'i', 'o', 'u'], sentence_list))
  return words_begin_with_vowel

if __name__ == '__main__':
  while(True):
    sentence = input('Please enter a sentence : ')
    print(re.sub(r'\s+', '', sentence))
    if re.sub(r'\s+', '', sentence).isalpha():
      break
    else:
      print('Please enter a non-numeric value\n')

  words_with_vowels = words_beginning_with_vowel(sentence)
  print(f'These are the words that begin with a vowel : {words_with_vowels}')
