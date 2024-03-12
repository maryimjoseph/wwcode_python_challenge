# Day 48 : Create a program that replaces specific words in a text with their synonyms

# This script takes a word and a phrase as inputs and
# replaces all occurences of the word in the phrase with its synomym.

import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
import random

def replace_with_synonym(p_word, p_phrase):
  # https://www.holisticseo.digital/python-seo/nltk/wordnet  
  word = p_word.lower()
  phrase = p_phrase.lower()
  synonyms = []

  for syn in wordnet.synsets(p_word):
    for i in syn.lemmas():
      synonyms.append(i.name())

  synonyms = list(set(synonyms))

  index = random.randint(0, len(synonyms)-1)
  synonym = synonyms[index]
  return p_phrase.replace(p_word, synonym)

if __name__ == '__main__':
  word = input('Enter a word : ')
  phrase = input('Enter a phrase : ')
  print(replace_with_synonym(word, phrase))
