def linear_search(arr, target):
    for item in arr:
        if item == target:
            return True

    return False

arr = [0, 1, 2, 3, 4, 5]

print(linear_search(arr, 0))
print(linear_search(arr, 5))
print(linear_search(arr, 10))
