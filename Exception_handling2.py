# program for handling multiple error with one except
# statement

def fun(a):
    if a<4:
        # throw ZeroDivisionError for a=3
        b = a/(a-3)
    # throw NameError if a>=4
    # print("Value of b : ",b) # error occured 

try:
    fun(3)
    #fun(5)

except ZeroDivisionError:
    print("ZeroDivisionError occurred and Handled")
except NameError :
    print("NameError occurred and handled")