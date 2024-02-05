def mul(*args):
    #arg is a tuple. passing a tuple as args will make it a tuple of tuples
    m=1
    for arg in args:
        m *= arg
    return m

print(mul(2,3,4))

def add(x,y):
    return x+y

nums = [2,5]

print(add(*nums))

n = { "x":2, "y":7}
print(add(**n))

def calculate(*args,operator):
    #here operator must be a named arguement or it will be added to args
    if(operator == "+"):
        return sum(args)
    elif(operator =="*"):
        return mul(*args)
    # passing args would have resulted in a tuple of tuples. so we need to unpack args with *args


print(calculate(2,4,5,operator="*"))

####### unpacking keyword arguments #######

def named(**kwargs):
    #turns keyword arguments into a dictionary
    print(kwargs)
named(first="bob",last="marley")
#if we had a dictionary of keyword  arguments
#named(**dic)