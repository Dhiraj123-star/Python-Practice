# closure in Python for simple adder
# 
def f1(x):
    def f2(y):
        return x+y
    return f2

# driver code
adder = f1(9)
print(adder(90))

