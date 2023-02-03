# exception handling in Python with try,except and else

try:
    num1=int(input("Enter your numerator: "))
    num2=int(input("Enter your denominator: "))
    division=num1/num2
    print(f"The result is: {division}")
except:
    print("Invalid Input")
else:
    print("Division is successful!!")
