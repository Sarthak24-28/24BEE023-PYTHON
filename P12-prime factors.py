def prime_factors(n, divisor=2):
    if n == 1:
        return []
    
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    else:
        return prime_factors(n, divisor + 1)

number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    factors = prime_factors(number)
    print("Prime factors:", factors)
