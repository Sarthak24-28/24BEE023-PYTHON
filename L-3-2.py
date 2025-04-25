#L-3-2

def to_lowercase(s):
    result = ''
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)  
        else:
            result += char
    return result


def to_uppercase(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)  
        else:
            result += char
    return result


def toggle_case(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)  
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)  
        else:
            result += char
    return result


input_str = input("Enter a string: ")

print("Lowercase:", to_lowercase(input_str))
print("Uppercase:", to_uppercase(input_str))
print("Toggle Case:", toggle_case(input_str))
