# Day 34 : Write a Python program to merge two dictionaries

# This script merges two dictionaries and 
# displays the merged dictionary.

#  Dictionaries and lists are passed by referene to functions
def merge_dictionarys(p_dict_1, p_dict_2):
  p_dict_1.update(p_dict_2)

if __name__ == '__main__':
  v_dict_states_1 = {'CA':'California', 'TX':'Texas', 'OH':'Ohio'}
  v_dict_states_2 = {'AZ':'Arizona', 'NV':'Nevada', 'UT':'Utah'}

  print(f'Dictionary 1 : {v_dict_states_1}')
  print(f'Dictionary 2 : {v_dict_states_2}')

  merge_dictionarys(v_dict_states_1, v_dict_states_2)

  print(f'Updated Dictionary after merger : {v_dict_states_1}')
