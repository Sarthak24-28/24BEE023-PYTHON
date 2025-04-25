#L-5-4
import random


random_numbers = [random.randint(-30, 30) for _ in range(30)]
print("Original list of 30 random numbers:", random_numbers)


positive_numbers = [num for num in random_numbers if num > 0]
negative_numbers = [num for num in random_numbers if num < 0]


print("\nList of positive numbers:", positive_numbers)
print("List of negative numbers:", negative_numbers)
