def reverse_list(numbers):
    if len(numbers) == 0:
        return []
    
    return reverse_list(numbers[1:]) + [numbers[0]]

input_list = list(map(int, input("Enter a list of numbers (space-separated): ").split()))
reversed_list = reverse_list(input_list)
print("Reversed list:",reversed_list)
