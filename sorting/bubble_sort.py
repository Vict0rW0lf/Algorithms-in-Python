def bubble_sort(arr, length):

    for i in range(length - 1):
        for j in range((length - i) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


arr = [10, 200, 0, -2, 900, 67, 5, 1, 70]

bubble_sort(arr, len(arr))

print(arr)
