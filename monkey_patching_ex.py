# monkey patching in Python

import math_operations

# define our custom multiply  function

def multiply(a,b):
    return a*b

# monkey patching : Replacing the add function with multiply

math_operations.add = multiply

# now calling add it will perform multiply operations 

result = math_operations.add(12,4)

print(f'The result is {result}')