# try-except with else statement

try:
    num=int(input("Enter your number: "))
    assert num%2==0
except:
    print("Not an Even number")
else:
    reciprocal=1/num
    print("The reciprocal is",reciprocal)

