# O(n)

# A Set is an unordered collection data type that is iterable,
# mutable and has no duplicate elements. Python’s set class represents
# the mathematical notion of a set.
# The major advantage of using a set, as opposed to a list,
# is that it has a highly optimized method for checking whether a specific
# element is contained in the set. This is based on a data structure known as
# a hash table. Since sets are unordered, we cannot access items
# using indexes like we do in lists.

def first_duplicate(arr):
    # Python set 
    holder = set()

    for item in arr:
        if item in holder:
            return item
        else:
            holder.add(item)

    return -1

arr = [2, 1, 3, 5, 3, 2]
arr1 = [2, 4, 1, 3, 5, 6]

print(first_duplicate(arr))
print(first_duplicate(arr1))


    
