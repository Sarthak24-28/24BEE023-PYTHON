def compute(n):
    n = str(n) 
    term1 = int(n)
    term2 = int(n * 2)
    term3 = int(n * 3)
    term4 = int(n * 4)
    return term1 + term2 + term3 + term4

for i in range(4, 8):
    result = compute(i)
    print(f"compute({i}) = {result}")
