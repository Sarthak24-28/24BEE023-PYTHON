def sum_avg(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    average = total / 5
    return total, average

print("Enter marks for five subjects:")

m1 = int(input("Subject 1: "))
m2 = int(input("Subject 2: "))
m3 = int(input("Subject 3: "))
m4 = int(input("Subject 4: "))
m5 = int(input("Subject 5: "))

total, average = sum_avg(m1, m2, m3, m4, m5)

print("\nTotal Marks:", total)
print("Average Marks:", average)
