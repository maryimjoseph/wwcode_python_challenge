# Day 27 : Create a program that sorts a list of strings alphabetically

# Forms a list of strings after taking 5 strings as input
# and then sorts the list of strings alphabetically

def p_sort_list_strings(p_string_list): # v_string_list gets passed by reference
  p_string_list.sort()

if __name__ == '__main__':
  v_string_list = []
  for i in range(5):
    v_string = input(f'Enter a string#'+ str(i+1) + ' : ')
    v_string_list.append(v_string)
    
  print(f'\nOriginal list of strings : \n{v_string_list}')
  p_sort_list_strings(v_string_list)
  print(f'\nSorted list of strings : \n{v_string_list}')
