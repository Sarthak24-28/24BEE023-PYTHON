import math

class Solid:
    def __init__(self, solid_type, **dimensions):
        self.solid_type = solid_type
        self.dimensions = dimensions

    def surface_area(self):
        if self.solid_type == "sphere":
            return 4 * math.pi * self.dimensions["radius"]**2
        elif self.solid_type == "cylinder":
            r, h = self.dimensions["radius"], self.dimensions["height"]
            return 2 * math.pi * r * (r + h)
        elif self.solid_type == "cuboid":
            l, w, h = self.dimensions["length"], self.dimensions["width"], self.dimensions["height"]
            return 2 * (l * w + l * h + w * h)

    def volume(self):
        if self.solid_type == "sphere":
            return (4/3) * math.pi * self.dimensions["radius"]**3
        elif self.solid_type == "cylinder":
            r, h = self.dimensions["radius"], self.dimensions["height"]
            return math.pi * r**2 * h
        elif self.solid_type == "cuboid":
            l, w, h = self.dimensions["length"], self.dimensions["width"], self.dimensions["height"]
            return l * w * h

# Example usage:
sphere = Solid("sphere", radius=5)
cylinder = Solid("cylinder", radius=3, height=7)
cuboid = Solid("cuboid", length=4, width=6, height=8)

print("Sphere Surface Area:", sphere.surface_area())
print("Sphere Volume:", sphere.volume())

print("\nCylinder Surface Area:", cylinder.surface_area())
print("Cylinder Volume:", cylinder.volume())

print("\nCuboid Surface Area:", cuboid.surface_area())
print("Cuboid Volume:", cuboid.volume())
