#L-4-3

input_str = input("Enter a string: ")


alphabet_count = 0
digit_count = 0


for ch in input_str:
    ascii_val = ord(ch)
    if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):  
        alphabet_count += 1
    elif 48 <= ascii_val <= 57:  
        digit_count += 1

print("Number of alphabets:", alphabet_count)
print("Number of digits:", digit_count)
