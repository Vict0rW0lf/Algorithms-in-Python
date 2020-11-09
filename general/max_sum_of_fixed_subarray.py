'''

    Finding the max sum of a subarray of fixed size K

    This was done with the sliding window technique

'''


def max_sum(arr, k):

    if len(arr) < k:
        raise Exception('List is smaller than target sum')
    
    max_value = 0
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if i >= k - 1:
            max_value = max(max_value, current_sum)
            current_sum -= arr[i - (k - 1)]

    return max_value
    

arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]

print(max_sum(arr, 3))
print(max_sum([1, 2], 3))


