#L-8-3
names_set = set()


names_set.add("Alice")
names_set.add("Bob")
names_set.add("Charlie")
names_set.add("David")
names_set.add("Eve")


names_set.remove("Bob")  
names_set.add("Bobby")   


names_set.remove("Charlie")  
names_set.remove("Eve")     

print("Final set of names:", names_set)
