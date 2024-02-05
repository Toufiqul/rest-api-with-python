import functools
user = {"usename":"soething","role":"admin"}

def getAdminPassword():
    return "1234"

def makeSecure(func):
    def secureFunction():
        if(user["role"] == "admin"):
            return func()
    return secureFunction

getAdminPassword = makeSecure(getAdminPassword)

print(getAdminPassword())


##instead of getAdminPassword = makeSecure(getAdminPassword)declare getAdminPassword with @makeSecure  (at syntax)

@makeSecure
def getAdminPassword():
    return "1234"


def makeSecure(func):
    @functools.wraps(func) #need this line to keep the getAdminPassword function in python and keep its documentation
    def secureFunction():
        if(user["role"] == "admin"):
            return func()
    return secureFunction


### to pass parameters to getAdminPassword ###

@makeSecure
def getAdminPassword(panel):
    if panel=="admin":
        return "1234"
    elif panel=="billing":
        return "12345678"

def makeSecure(func):
    @functools.wraps(func) #need this line to keep the getAdminPassword function in python and keep its documentation
    def secureFunction(*args, **kwargs):
        if(user["role"] == "admin"):
            return func(*args, **kwargs)
    return secureFunction

### passing parameters to Decorators ###