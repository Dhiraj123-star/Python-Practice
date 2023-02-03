# function that accept an another function as an argument called
# higher-order function

def add(x):
    return x+1
def sub(n):
    return n-1

def operator(func,x):
    temp= func(x)
    return temp

print(operator(add,12))
print(operator(sub,0))