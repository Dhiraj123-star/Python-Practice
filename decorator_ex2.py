# python provides the facility to define the function inside another function
# these types of functions called inner functions
def func1():
    print("Hello I'm first function")
    def func2():
        print("I'm second function")
        def func3():
            print("I'm third function")
        func3()
    func2()
func1()