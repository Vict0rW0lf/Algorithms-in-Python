import util

def bubble_sort(arr):  
  for i in range(len(arr)):    
    for j in range(len(arr) - 1 - i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swap = True

    if swap == False:
      break;

    swap = False

arr = util.randomized_arr

bubble_sort(arr)

print(arr)