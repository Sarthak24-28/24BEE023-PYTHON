#L-3-4

main_str = input("Enter the main string: ")
sub_str = input("Enter the string to remove: ")


len_main = 0
for _ in main_str:
    len_main += 1

len_sub = 0
for _ in sub_str:
    len_sub += 1


i = 0
found = False
start_index = -1


while i <= len_main - len_sub:
    match = True
    for j in range(len_sub):
        if main_str[i + j] != sub_str[j]:
            match = False
            break
    if match:
        start_index = i
        found = True
        break
    i += 1

final_str = ""

if found:
    
    for k in range(start_index):
        final_str += main_str[k]
    
    for k in range(start_index + len_sub, len_main):
        final_str += main_str[k]
else:
    
    for ch in main_str:
        final_str += ch


print("Final string:", final_str)
