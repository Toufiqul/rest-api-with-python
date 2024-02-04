def add(x,y):
    return x+y

print(add(1,4))

add = lambda x,y:x+y
print(add(1,5))

print((lambda x,y:x+y)(2,5))

def double(x):
    return x*2

seq =range(1,5)

doubled = [x*2 for x in seq]
doubled = [double(x) for x in seq]
doubled = [(lambda x:x*2)(x) for x in seq]
doubled = list(map(double,seq))
doubled = list(map(lambda x:x*2,seq))