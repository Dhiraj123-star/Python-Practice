# try with else clause

def AbyB (a,b):
    try:
        c= ((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result is 0")
    else:
        print(c)

# driver code 
AbyB(2.0,3.0)
AbyB(3.0,3.0)