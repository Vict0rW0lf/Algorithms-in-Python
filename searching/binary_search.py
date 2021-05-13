#needs a sorted array
arr = [-16, 1, 20, 99, 200, 333, 400, 999]

# O(log n)
def binary_search(arr, target):
  start = 0
  end = len(arr) - 1

  while start <= end:
      mid = (start + end) // 2

      if target == arr[mid]:
          return True
      elif target > arr[mid]:
          start = mid + 1
      else:
          end = mid - 1

  return False


