import math
x_center, y_center = map(float, input("Enter the coordinates of the center (x, y): ").split())
radius = float(input("Enter the radius of the circle: "))
x_point, y_point = map(float, input("Enter the coordinates of the point (x, y): ").split())

distance = math.sqrt(pow(x_point - x_center, 2) + pow(y_point - y_center, 2))
5
if distance < radius:
    print("The point lies inside the circle.")
elif distance == radius:
    print("The point lies on the circle.")
else:
    print("The point lies outside the circle.")

