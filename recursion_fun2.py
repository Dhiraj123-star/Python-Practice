# another example of recursion function in Python
def dispN(n):
    if n==0:
        return 
    print(n)
    dispN(n-1)

# driver code

num = int(input("Enter your number: "))
dispN(num)

