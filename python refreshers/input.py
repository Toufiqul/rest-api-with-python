# x= input() #promptless
# y= input("prompt") #prompt
 
# print(x)
# print(y)

# input() returns a STRING

x = input("input x") 
x=int(x) #type conversion to int. probably just created a new object
y=2*x
print("two times x: " + str(y))
print(f"two times x: {y}")
print(f"two times x: {y:.2f}")

# :.2f to print first 2 decimal points