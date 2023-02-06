# assert keyword
# it simply takes input boolean condition, when returns 
# True doesn't return anything otherwise returns AssertionError

try:
    x=1
    y=0
    assert y!=0 , "Division by zero , not possible!!"
    print(x/y)
except  AssertionError as msg:
    print(msg)
print("The rest of the program still runs!!")