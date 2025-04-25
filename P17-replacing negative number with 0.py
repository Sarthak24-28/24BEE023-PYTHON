def sanitize_list(lst, index=0):
    if index == len(lst):
        return lst
    
    if lst[index] < 0:
        lst[index] = 0
    
    return sanitize_list(lst, index + 1)

input_list = list(map(int, input("Enter a list of numbers (space-separated): ").split()))
sanitized_list = sanitize_list(input_list)
print("Sanitized list:",sanitized_list)
