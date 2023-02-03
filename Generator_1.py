# generator Example in Python
def generateNum(n):
    # initialise counter
    value=0
    # loop until counter is less than n 
    while value <n:
        # produce the current value of the counter 
        yield value 

        # increment the counter 
        value+=1

# iterate over the generator object produced
for value in generateNum(8):
    print(value)