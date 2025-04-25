#L-6-1
def count_boys_and_girls(names_list):
    boys_count = 0
    girls_count = 0

    for name in names_list:
        if isinstance(name, tuple):  
            boys_count += 1
        else:  
            girls_count += 1

    return boys_count, girls_count

names = ['Shubha', 'Nisha', 'Sudha', ('Suresh',), ('Rajesh',), 'Radha']
boys, girls = count_boys_and_girls(names)
print(f"Boys: {boys}, Girls: {girls}")
