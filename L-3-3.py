#L-3-3

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")


len1 = 0
for _ in str1:
    len1 += 1


len2 = 0
for _ in str2:
    len2 += 1

found = False


for i in range(len2 - len1 + 1):
    match = True
    for j in range(len1):
        if str2[i + j] != str1[j]:
            match = False
            break
    if match:
        found = True
        break


if not found:
    for i in range(len1 - len2 + 1):
        match = True
        for j in range(len2):
            if str1[i + j] != str2[j]:
                match = False
                break
        if match:
            found = True
            break


if found:
    print("One string is present in the other.")
else:
    print("No string is present in the other.")
