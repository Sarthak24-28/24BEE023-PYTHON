# L-4-11
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def sin_x(x, terms=10):
    result = 0
    for n in range(terms):
        
        power = (2 * n + 1)
        term = ((-1) ** n) * (x ** power) / factorial(power)
        result += term
    return result


degrees = float(input("Enter x (in degrees): "))


x_radians = degrees * 3.14159 / 180


result = sin_x(x_radians)
print(f"sin({degrees} degrees) ≈ {result}")
