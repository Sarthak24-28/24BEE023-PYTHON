# L-6-2
students = [
    ('A101', 'Shubha', 23),
    ('A104', 'Nisha', 23),
    ('A111', 'Sudha', 23)
]


roll_nos = []
names = []
ages = []


for student in students:
    roll_nos.append(student[0])
    names.append(student[1])
    ages.append(student[2])

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)
