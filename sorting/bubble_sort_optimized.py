def bubble_sort(arr):  
  for i in range(len(arr)):    
    for j in range(len(arr) - 1 - i):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swap = True

    if swap == False:
      break;

    swap = False

arr = [0, -11, 2, 99, 100, 0, 0, 1, 230829]

bubble_sort(arr)

print(arr)