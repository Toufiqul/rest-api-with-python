#functions used as parameters
def divide(a,b):
    if b==0:
        raise ZeroDivisionError("cant divide by zero")
    return a/b

def calculate(a,b,operation):
    return operation(a,b)

result = calculate(20,5,operation=divide)
print(result)