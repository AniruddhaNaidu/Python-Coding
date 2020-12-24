#DECORATORS
def details(name,surname):
    print(name,surname)

def smart(func):

    def inner(x,y):                            #decorator
        if x=='saxena' and y=='ankur':
            x,y=y,x
        return func(x,y)
    return inner

f=smart(details)
f('saxena','ankur')

#Eg2
def div(x,y):
    print(x/y)

def smart_div(func):
    def inner_fun(x,y):
        if x<y:
            x,y=y,x
        return func(x,y)
    return inner_fun

t=smart_div(div)
t(2,8)
















