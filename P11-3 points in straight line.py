x1= int(input("Enter x1"))
x2= int(input("Enter x2"))
x3= int(input("Enter x3"))
y1= int(input("Enter y1"))
y2= int(input("Enter y2"))
y3= int(input("Enter y3"))

if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("The points are collinear (fall on the same straight line).")
else:
    print("The points do not fall on the same straight line.")
