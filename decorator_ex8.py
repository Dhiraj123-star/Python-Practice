from mod_decorator1 import do_twice

@do_twice

def myfunc(*n):
    print(f"Hello {n}")

# call the function
myfunc("Dhiraj","Rahul")