# decorators are functions that takes another function as an argument
# to modify its behaviour without changing function itself

def smart_divide(func):
    def inner(a,b):
        print("Dividing ",a, "by ",b)
        if b==0:
            print("Please make sure denominator shouldn't be zero!!")
        return func(a,b)
    return inner
@smart_divide
def divide(a,b):
    print(a/b)
divide(1,0)