from  monkey import A
def monkey_f(self):
    print("monkey_f() is being called")

A.func=monkey_f # replacing address of "func" with "monkey_f"
obj= A()

# calling function "func" whose address got replaced with function "monkey_f()"
obj.func()
