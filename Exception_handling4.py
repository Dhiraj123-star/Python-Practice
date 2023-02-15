# use of finally statement

try:
    k=6//0
except ZeroDivisionError:
    print("can't divide by zero")
finally:
    print("This statement is always executed")
