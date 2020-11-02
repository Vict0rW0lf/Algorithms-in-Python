def sum_of_two(a, b, target):

    holder = set()

    for num in a:
        holder.add(target - num)

    for num in b:
        if num in holder:
            return True

    return False

a = [0, 0, -5, 30212]
b = [-10, 40, -3, 9]

print(sum_of_two(a, b, -8))
print(sum_of_two(a, b, -10))
print(sum_of_two(a, b, 25))
