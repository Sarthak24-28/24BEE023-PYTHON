def power(a, b):
    if b == 0:
        return 1
    elif b > 0:
        return a * power(a, b - 1)
    else:
        return 1 / power(a, -b)

a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))

result = power(a, b)
print(result)
