def create_tuples(ending_value):
    result = [(x, x**2, x**3) for x in range(1, ending_value + 1)]
    return result

ending_value = int(input("Enter the ending value: "))
result = create_tuples(ending_value)

print("List of tuples:",result)
