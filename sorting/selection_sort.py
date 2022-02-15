import util


def selection_sort(arr):
    for i in range(len(arr)):
        smallest = i

        for j in range(i, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j

        arr[i], arr[smallest] = arr[smallest], arr[i]


arr = util.randomized_arr

selection_sort(arr)

print(arr)
