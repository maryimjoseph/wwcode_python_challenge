# Day 50 : Create a program that finds the intersection and union of two sets

# Takes 2 lists of elements as inputs, converts them to sets
# and prints the result of the Intersection and Union of the two sets.

def set_intersection(p_set_1, p_set_2):
  return p_set_1.intersection(p_set_2)

def set_union(p_set_1, p_set_2):
  return p_set_1.union(p_set_2)

if __name__ == '__main__':
  set_1 = set(input('Enter elements of the first set separated by commas : ').split(','))
  set_2 = set(input('Enter elements of the second set separated by commas : ').split(','))

  print(f'Intersection of Set#1 and Set#2 is : {set_intersection(set_1, set_2)}')
  print(f'Union of Set#1 and Set#2 is : {set_union(set_1, set_2)}')
