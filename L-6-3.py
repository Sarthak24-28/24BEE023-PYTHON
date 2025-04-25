#L-6-3
from datetime import date


date1 = (13, 12, 2018)
date2 = (25, 2, 2019)


d1 = date(date1[2], date1[1], date1[0]) 
d2 = date(date2[2], date2[1], date2[0])


delta = abs(d2 - d1)


print(f"Number of days between {date1} and {date2}: {delta.days} days")
