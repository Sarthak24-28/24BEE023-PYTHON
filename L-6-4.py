# L-6-4
menu = [
    ('Pizza', 300),
    ('Burger', 150),
    ('Pasta', 200),
    ('Sandwich', 100),
    ('Salad', 120)
]


sorted_menu = sorted(menu, key=lambda x: x[1], reverse=True)


print("Menu sorted by price (highest to lowest):")
for item, price in sorted_menu:
    print(f"{item}: ₹{price}")
