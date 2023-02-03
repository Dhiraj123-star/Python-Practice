# decorator function which returns twice value of the function
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice