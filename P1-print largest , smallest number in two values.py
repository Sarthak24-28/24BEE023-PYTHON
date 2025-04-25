num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print("Largest value:", num1)
    print("Smallest value:", num2)
elif num2 > num1:
    print("Largest value:", num2)
    print("Smallest value:", num1)
else:
    print("Both values are equal:", num1)
