# decorator using Python

def uppercase_decorator(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello {name}"

@uppercase_decorator
def goodbye(name):
    return f"Bye {name}"

# call the function

name = input("Enter your name: ")
print(greet(name))
print(goodbye(name))