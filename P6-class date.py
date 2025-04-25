class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        if isinstance(other, Date):
            return self.day == other.day and self.month == other.month and self.year == other.year
        return False

    def __str__(self):
        return f"{self.day:02}/{self.month:02}/{self.year}"

date1 = Date(15, 8, 2022)
date2 = Date(15, 8, 2022)
date3 = Date(1, 1, 2023)

print("Is Date1 equal to Date2?",date1 == date2)
print("Is Date1 equal to Date3?",date1 == date3)

print("Date 1:",date1)
print("Date 2:",date2)
print("Date 3:",date3)
