name = "something"

greetings = f"hello {name}"

print(greetings)
print(f"hello {name}")
name = "something else"
print(f"hello {name}")

# string.format() takes a string and replaces the {} with the parameter passed and returns a new string

st = "hello {}"
newSt = st.format("world")
print(newSt)

# for multiple parameters:

multiSt = "hello {} and {}"
newSt = multiSt.format("world", "everyone else")
print(newSt)