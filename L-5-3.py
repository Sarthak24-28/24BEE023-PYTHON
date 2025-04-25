#L-5-3
import random

random_numbers = [random.randint(1, 30) for _ in range(50)]
print("Original list of 50 random numbers:", random_numbers)

unique_numbers = list(set(random_numbers))

print("\nList after removing duplicates:", unique_numbers)
