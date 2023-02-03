# parameterised decorator function
def divide(x,y):
    print(x/y)

def outer_divide(func):
    def inner(x,y):
        x,y=y,x
        return func(x,y)
    return inner

divide1 = outer_divide(divide)
divide1(2,4)