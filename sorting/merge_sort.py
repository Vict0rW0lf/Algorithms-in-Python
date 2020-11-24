def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

arr = create_array()

def merge(a, b):
    c = []
    a_idx, b_idx = 0,0

    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx+=1
        else:
            c.append(b[b_idx])
            b_idx+=1

    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])

    return c

#Time O(n log n) Space O(n)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left, right = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])

    return merge(left, right)

print(arr)
print(merge_sort(arr))
    

    



