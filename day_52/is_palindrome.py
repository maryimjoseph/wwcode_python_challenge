# Day 52 : Create a program that checks if a string is a palindrome

# Takes a string input and displays if the input word is a palindorme

# A Palindrome is a word, phrase, or sequence that reads the same backward as forward
# Examples : civic, madam, radar
def is_palindrome(p_word):
   word_reverse = p_word[::-1]
   if p_word == word_reverse:
     return True
   else:
     return False

if __name__ == '__main__':
  while(True):
    word = input('Enter a word : ')
    if word.isalpha():
      break
    else:
      print('Please enter a non-numeric value\n')

  message = 'The word "' + word + ('" is a Palindrome' if is_palindrome(word) else '" is not a Palindrome')
  print(message)
