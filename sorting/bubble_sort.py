import util

def bubble_sort(arr, length):

    for i in range(length):
        for j in range((length - i) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


arr = util.randomized_arr

bubble_sort(arr, len(arr))

print(arr)
