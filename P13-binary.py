def binary(n):
    if n == 0:
        return ''
    print(f"n: {n}, n//2: {n//2}, n%2: {n % 2}")
    return binary(n//2) + str(n % 2)


n = int(input("Enter a number: "))
print(binary(n))
