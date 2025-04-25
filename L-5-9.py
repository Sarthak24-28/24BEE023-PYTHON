# L-5-9
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60]


list3 = [num for num in list1 if num not in list2]


print("First List:", list1)
print("Second List:", list2)
print("Third List (Numbers from list1 not in list2):", list3)
