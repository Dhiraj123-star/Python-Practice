# To check perfect number in Python
# finding the square of the given number and convert into integer 
# apply the square to the square root number and check if it's
# perfect square root
# return the result as boolean

def checkPerfect(num):
    square = int(num**0.5)
    return (num==square**2) # return True or False 

# driver code

print(checkPerfect(36)) # returns True
print(checkPerfect(10)) # returns False 

