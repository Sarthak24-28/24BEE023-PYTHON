def calculate_average(lst, index=0, total=0):
    if index == len(lst):
        return total / len(lst) if len(lst) > 0 else 0
    
    total += lst[index]
    
    return calculate_average(lst, index + 1, total)

input_list = list(map(int, input("Enter a list of numbers (space-separated): ").split()))
average = calculate_average(input_list)
print("The average of the numbers in the list is:",average)
