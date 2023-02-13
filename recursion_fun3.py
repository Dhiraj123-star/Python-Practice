# calculate the factorial of the input number 

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

# driver code
num = int(input("Enter your number: "))
print(fact(num))


