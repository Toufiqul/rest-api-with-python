li = ["something","something else","other things","something"]
tuples = ("something","something else","other things","something") #immutable
sets = {"something","something else","other things","something"} #unique,sorted
sets2 = {"something","something else","something"} #unique,sorted

# sets[i] doesnt work because order might be different
li.append("fsdf")
li.remove("something")

print(sets.difference(sets2)) # A-B
print(sets2.difference(sets))
print(sets2.union(sets)) # A U B
print(sets2.intersection(sets)) # A A B

print("something" in sets)
# also works for lists,tuples,strings