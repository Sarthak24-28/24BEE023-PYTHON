with open("test1.txt", "r") as src, open("test2.txt", "w") as dest:
    for line in src:
        upper_line = line.upper()
        dest.write(upper_line)

print("Contents copied from source file to destination file with all lowercase converted to uppercase.")
