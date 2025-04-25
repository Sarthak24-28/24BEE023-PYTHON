import csv
student_data = {}

with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        rollno = int(row['Roll No'])
        name = row['Name']
        sub1 = int(row['Sub1'])
        sub2 = int(row['Sub2'])
        sub3 = int(row['Sub3'])
        total = sub1 + sub2 + sub3

        student_data[rollno] = {
            'Name': name,
            'Subject 1': sub1,
            'Subject 2': sub2,
            'Subject 3': sub3,
            'Total': total
        }

for roll, details in student_data.items():
    print(f"Roll No: {roll}")
    for key, value in details.items():
        print(f"  {key}: {value}")
    print()
