from mod_decorator import do_twice
@do_twice
def say_hello():
    print("Hello Python")

say_hello()
