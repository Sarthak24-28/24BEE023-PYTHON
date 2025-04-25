def count_alpha_digits(s):
    alpha_count = 0
    digit_count = 0
    
    for char in s:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():
            digit_count += 1
    
    return {"alphabets": alpha_count, "digits": digit_count}

input_string = input("Enter a string: ")
result = count_alpha_digits(input_string)

print("Count of Alphabets and Digits:", result)
