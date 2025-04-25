marks = []
for i in range(1, 4):
    entry = input(f"Enter marks for subject {i} (or 'A' for Absent): ")
    if entry.upper() == 'A':
        marks.append('A')
    else:
        marks.append(int(entry))

total = 0
count = 0
fail = False

print("\nSubject-wise Grades:")
for i in range(3):
    mark = marks[i]

    if mark == 'A':
        grade = 'NA'
        fail = True 
    elif 0 <= mark <= 39:
        grade = 'F'
        fail = True
        total += mark
        count += 1
    elif 40 <= mark <= 44:
        grade = 'P'
        total += mark
        count += 1
    elif 45 <= mark <= 49:
        grade = 'C'
        total += mark
        count += 1
    elif 50 <= mark <= 54:
        grade = 'B'
        total += mark
        count += 1
    elif 55 <= mark <= 59:
        grade = 'B+'
        total += mark
        count += 1
    elif 60 <= mark <= 69:
        grade = 'A'
        total += mark
        count += 1
    elif 70 <= mark <= 79:
        grade = 'A+'
        total += mark
        count += 1
    elif 80 <= mark <= 100:
        grade = 'O'
        total += mark
        count += 1
    else:
        grade = 'Invalid'
        fail = True 

    print(f"Subject {i+1}: Grade - {grade}")

if count > 0:
    average = total / count
    print(f"\nTotal Marks: {total}")
    print(f"Average Marks: {average:.2f}")
else:
    print("\nNo valid marks to calculate total and average.")

if fail:
    print("Result: FAIL")
else:
    print("Result: PASS")
