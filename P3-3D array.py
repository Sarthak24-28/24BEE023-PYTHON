def create_array(x, y, z, initial_value):
    array = []
    for i in range(x):
        plane = []
        for j in range(y):
            row = []
            for k in range(z):
                row.append(initial_value)
            plane.append(row)
        array.append(plane)
    return array

result = create_array(3,4,5,'n')

for i in range(len(result)):
    print("Plane",i+1)
    for row in result[i]:
        print(row)
    print()
