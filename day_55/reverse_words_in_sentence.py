# Day 55 : Create a function that takes a string and returns the reverse of each word

# Takes in a phrase or sentence as input and
# returns the reverse of each of the words.

def reverse_words_in_sentence(p_sentence):
  list_of_words = p_sentence.split(' ')
  list_of_rev_words = list(map(lambda x:x[::-1], list_of_words))
  return list_of_rev_words

if __name__ == '__main__':
  sentence = input('Enter a sentence : ')
  rev_words = reverse_words_in_sentence(sentence)
  print(f'Here is the sentence with its words reversed : \n {rev_words}')
