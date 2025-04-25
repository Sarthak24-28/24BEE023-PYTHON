import math
class Shape:
    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def perimeter(self):
        if self.shape_type == "circle":
            return 2 * math.pi * self.dimensions["radius"]
        elif self.shape_type == "square":
            return 4 * self.dimensions["side"]
        elif self.shape_type == "rectangle":
            return 2 * (self.dimensions["length"] + self.dimensions["width"])
        elif self.shape_type == "triangle":
            return sum(self.dimensions.values())

    def area(self):
        if self.shape_type == "circle":
            return math.pi * self.dimensions["radius"]**2
        elif self.shape_type == "square":
            return self.dimensions["side"]**2
        elif self.shape_type == "rectangle":
            return self.dimensions["length"] * self.dimensions["width"]
        elif self.shape_type == "triangle":
            a, b, c = self.dimensions["side1"], self.dimensions["side2"], self.dimensions["side3"]
            s = (a + b + c) / 2
            return math.sqrt(s * (s - a) * (s - b) * (s - c))

circle = Shape("circle", radius=5)
print("Circle Perimeter:", circle.perimeter())
print("Circle Area:", circle.area())

square = Shape("square", side=4)
print("\nSquare Perimeter:", square.perimeter())
print("Square Area:", square.area())

rectangle = Shape("rectangle", length=6, width=3)
print("\nRectangle Perimeter:", rectangle.perimeter())
print("Rectangle Area:", rectangle.area())

triangle = Shape("triangle", side1=3, side2=4, side3=5)
print("\nTriangle Perimeter:", triangle.perimeter())
print("Triangle Area:", triangle.area())
