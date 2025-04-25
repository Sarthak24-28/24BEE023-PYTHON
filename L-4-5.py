# L-4-5
max_side = 30

print("Pythagorean Triplets (a, b, c) where a, b, c <= 30:")


for a in range(1, max_side + 1):
    for b in range(a, max_side + 1):  
        for c in range(b, max_side + 1):  
            if a**2 + b**2 == c**2:
                print(f"({a}, {b}, {c})")
