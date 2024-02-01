li = [2,3,4,5,6,7,8,9,10,11,12,13]
l=[]
for i in li:
    if i%2==0:
        l.append(i)

li1 = [2,3,4,5,6,7,8,9,10,11,12,13]
twoLi = [i*2 for i in li1]
# [ {what you want to fo} {loop}]
l1=[i for i in li1 if i%2==0]
# [{var to add} {loop} {condition}]
print(l1)
print(twoLi)

# string.startswith("C") returns boolean
# id({var/list}) returns id. associated with memory address but not real address

li = [2,3,4,5,6,7,8,9,10,11,12,13]
l=[]

l=li
print(f"li id : {id(li)}")
print(f"l id : {id(l)}")
#returns the same id. but changing li doesnt change l

li = []

print(li)
print(l)