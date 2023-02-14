# closure in Python

def divider(y):
    def divide(x):
        return x/y
    return divide 

# driver code

d1 = divider(2)
d2= divider(5)
d3= divider(4)

print(d1(2))
print(d2(9))
print(d3(10))