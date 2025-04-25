def count_lower_upper(s):
    lower_count = 0
    upper_count = 0

    for char in s:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1

    return {"lowercase": lower_count, "uppercase": upper_count}


a=input("Enter string")
result = count_lower_upper(a)

print("Input String:", a)
print("Result:", result)
