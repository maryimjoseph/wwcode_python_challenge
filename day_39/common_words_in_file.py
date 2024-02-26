# Day 39 : Write a program to find the most common words in a text file

# Prints the top 10 common words in a text file 
# along with the number of their occurrences.

# poem.txt
'''
TWINKLE, TWINKLE, LITTLE STAR

Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.

When the blazing sun is set, and the grass with dew is wet. Then you show your little
light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
are.

Then the traveler in the dark thanks you for your tiny spark. How could he see where to
go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.

As your bright and tiny spark lights the traveler in the dark, though I know not what you
are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.
'''

def count_words_in_file(p_file, p_dict):
  for line in p_file:
    v_word_list = line.split()

    for word in v_word_list:
      word = word.lower().strip(' ,.?')

      if p_dict.get(word) is None:
        p_dict[word] = 1
      else:
        p_dict[word] = p_dict[word] + 1

  p_dict_sorted = dict(sorted(p_dict.items(), key=lambda x: x[1], reverse=True))
  return p_dict_sorted

    
if __name__ == '__main__':
  v_dict = {}
  v_file = open('poem.txt', 'r')

  v_dict_sorted = count_words_in_file(v_file, v_dict)
  print(f'Sorted dictionary : \n {v_dict_sorted}')
 
  v_count = 0
  print('\nTop 10 common words : ')
  for k, v in v_dict_sorted.items():
    print(k, ':', v)
    v_count+=1
    if v_count == 10:
      break
      
  v_file.close()
