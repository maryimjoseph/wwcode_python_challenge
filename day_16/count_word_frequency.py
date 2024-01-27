# Day 16 : Write a function that counts the frequency of each word in a sentence.

# This script takes a sentence as an input and
# lists the frequency of each word in the sentence

if __name__ == '__main__':
  while(True):
    v_sentence = input('Please type in a sentence : ')
    if len(v_sentence) < 3 or v_sentence.strip(' ').count(' ') == 0:
      print('The entry is not a sentence. Please try again\n')
      continue
    else:
      break
  v_list_of_words = v_sentence.strip().split(' ')

  v_word_counts = []
  for i,w in enumerate(v_list_of_words):
    v_word_counts.append(v_list_of_words.count(w))

  print('\nBelow is the list of words and their counts in your sentence :\n')
  for w, cnt in set(zip(v_list_of_words, v_word_counts)):
    print(f"'{w}' occurs {'once' if cnt == 1 else 'twice' if cnt == 2 else str(cnt)+' times'}")
