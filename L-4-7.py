# L-4-7
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

n = int(input("Enter n: "))
r = int(input("Enter r: "))


nCr = factorial(n) // (factorial(r) * factorial(n - r))


nPr = factorial(n) // factorial(n - r)


print(f"nCr (Combination) of {n} and {r}: {nCr}")
print(f"nPr (Permutation) of {n} and {r}: {nPr}")
