# Day 51 : Create a program that counts the occurrences of each word in a text file

# Creates a text file, reads the contents of the file 
# counts the occurrence of each word in the file and
# lists the words and their counts.

def create_sample_file(p_fname):
  f = open(p_fname, 'w+')
  contents =  '''\
TWINKLE, TWINKLE, LITTLE STAR
Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
When the blazing sun is set, and the grass with dew is wet. Then you show your little
light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you are.
Then the traveler in the dark thanks you for your tiny spark. How could he see where to
go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
As your bright and tiny spark lights the traveler in the dark, though I know not what you
are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.'''
  f.write(contents)
  f.close()

def create_dict(p_fname):
  dict = {}
  file = open(p_fname, 'r')
  for line in file:
    for word in line.lower().strip('\n').split(' '):
      word_stripped = word.strip(',.?').strip('')
      if dict.get(word_stripped) is None:
        dict[word_stripped] = 1
      else:
        dict[word_stripped] += 1
  file.close()
  return dict

if __name__ == '__main__':
  create_sample_file('sample_text.txt')
  dict = create_dict('sample_text.txt')
  print(dict)
