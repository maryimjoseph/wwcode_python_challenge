# Day 10 : Write a program to remove duplicates from a list.

def input_list():
  v_string = input("Please enter a list of values separated by commas (,) : ")
  v_list = v_string.split(',')
  
  # To remove extraneous spaces before and afer the values of the list elements
  v_string_trimmed = ''
  for i in v_list:
    v_string_trimmed += i.strip()
    v_string_trimmed += ','
  v_string_trimmed = v_string_trimmed.rstrip(',')

  v_list = v_string_trimmed.split(',')
  return v_list

if __name__ == '__main__':
  v_clean_list = input_list()
  v_unique_list = set(v_clean_list)
  print(f'List with unique elements : {v_unique_list}')
