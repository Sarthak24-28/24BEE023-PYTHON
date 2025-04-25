#L-5-1
import random


odd_integers = [random.choice(range(1, 100, 2)) for _ in range(5)]
print("Original list of 5 odd integers:", odd_integers)


even_integers = [random.choice(range(2, 101, 2)) for _ in range(4)]
print("List of 4 even integers:", even_integers)


odd_integers[2] = even_integers
print("\nList after replacing the third element of odd integers with the even integers list:", odd_integers)


flattened_list = []
for item in odd_integers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)

print("\nFlattened list:", flattened_list)


flattened_list.sort()
print("\nSorted flattened list:", flattened_list)
