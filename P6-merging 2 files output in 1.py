with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2, open("merged_output.txt", "w") as output:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):
        if i < len(lines1):
            output.write(lines1[i].rstrip() + "\n")
        if i < len(lines2):
            output.write(lines2[i].rstrip() + "\n")

print("Lines from file1 & file2 merged alternately into output_path")

