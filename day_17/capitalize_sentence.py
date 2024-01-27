# Day 17 : Create a program that capitalizes the first letter of each word in a sentence

# This script takes a sentence as input and
# prints the sentence with the first letter of each word capitalized.
def capitalize_sentence(p_sentence):
  return v_sentence.title()

if __name__ == '__main__':
  while(True):
    v_sentence = input('Please input a sentence : ')
    if v_sentence.strip().count(' ') == 0 or len(v_sentence.strip()) < 3 :
      print('The entry is not a sentence.  Please try again.\n')      
      continue
    else:
      break
  print('\nBelow is the capitalized sentence : ')
  print(capitalize_sentence(v_sentence), '\n')
