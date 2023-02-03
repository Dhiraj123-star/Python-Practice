# chaining decorators means decorating a function with multiple
# decorators
def decort1(func):
    def inner():
        x=func()
        return x*x
    return inner

def decor(func):
    def inner():
        x=func()
        return 2*x
    return inner 

@decort1
@decor

def num():
    return 10

@decor
@decort1
def num2():
    return 10

print(num())
print(num2())
