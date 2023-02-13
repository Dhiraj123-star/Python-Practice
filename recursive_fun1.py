# recursion in Python

def sum(n):
    if n<=1:
        return n 
    else:
        ans= sum(n-1)
    return n+ans

# driver code

num = int(input("Enter your number: "))

print(sum(num))

