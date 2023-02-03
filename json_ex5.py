# to encode and decode operations
import json
var= {'age':45,'height':5}
x=json.dumps(var)
y=json.loads(x)
print(x)
print(y)

# when performing from a file 
with open("Sample.json" ,"r") as f:
    x= json.load(f)

print("From the file: ",x)