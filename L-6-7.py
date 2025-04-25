# L-6-7
tup = (1, 2, 3, 4, 5)


element_to_remove = 3

new_tup = tuple(x for x in tup if x != element_to_remove)

print(new_tup)
