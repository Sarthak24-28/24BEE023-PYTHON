# L-4-8
num = int(input("Enter a number to calculate its factorial: "))


factorial = 1


for i in range(1, num + 1):
    factorial *= i


print(f"The factorial of {num} is: {factorial}")
