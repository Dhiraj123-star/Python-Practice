# in python function is called first-class objects that means they can
# reference to, passed to a variable and returned from other functions 
# as well

def func1():
    print("Hello Python")

func2 = func1 # here we passed function to a variable
# both returns the same output 
func1()
func2()