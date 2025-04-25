# L-7-5
prices = {
    "apple": 2.5,  
    "banana": 1.2,
    "orange": 3.0,
    "milk": 1.5,
    "bread": 2.0
}


quantities = {
    "apple": 4,  
    "banana": 6,
    "orange": 3,
    "milk": 2,
    "bread": 1
}


total_bill = 0


for item in prices:
    if item in quantities:
        total_bill += prices[item] * quantities[item]

print(f"Total bill: ${total_bill:.2f}")
