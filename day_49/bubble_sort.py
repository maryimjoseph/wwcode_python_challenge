# Day 49 : Create a program that implements the bubble sort algorithm

# Sorts a list of numbers in ascending order, using the bubble sort algorithm

def bubble_sort(p_sample_list):
  sorted = False

  while not sorted:
    sorted = True
    for i in range( 0, len(sample_list) - 1):
      if sample_list[i] > sample_list[i+1]:
        sorted = False
        sample_list[i], sample_list[i+1] = sample_list[i+1], sample_list[i]
  return sample_list

if __name__ == '__main__':
  sample_list = [99, 105, 5, 3.6, 100]
  print(f'Sorted list : {bubble_sort(sample_list)}')
