# L-4-10
n = int(input("Enter the number N to generate the first N Fibonacci numbers: "))


a, b = 0, 1


print("Fibonacci series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b  
