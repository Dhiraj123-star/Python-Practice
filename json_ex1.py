import json
a = {"name":"John","age":45,"hobby":"Programming"}

b= json.dumps(a) # conversion to JSON done by dumps() function 
print(b)