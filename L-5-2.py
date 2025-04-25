#L-5-2
import random


random_numbers = [random.randint(1, 100) for _ in range(20)]
print("List of 20 random integers:", random_numbers)


num_to_find = int(input("Enter a number to find its positions in the list: "))


positions = [index for index, value in enumerate(random_numbers) if value == num_to_find]


if positions:
    print(f"The number {num_to_find} appears at positions: {positions}")
else:
    print(f"The number {num_to_find} is not found in the list.")
