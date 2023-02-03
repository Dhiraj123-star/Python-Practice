# lambda function acts as Anonymous function that takes as many arguments but
# return single value 

mylambda = lambda x,y,z: (x+y)*z - (x-y)

print(mylambda(12,3,2))
