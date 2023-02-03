# python program showing that json support different primitive types
import json
print(json.dumps(["Java","Python","JavaScript"])) # list conversion
print(json.dumps(("Welcome","to","Python"))) # tuple conversion
print(json.dumps("Python")) # string conversion
print(json.dumps(1234)) # number conversion
print(json.dumps(23.56)) # float conversion
print(json.dumps(True)) # boolean conversion to their respective values
print(json.dumps(False)) 
print(json.dumps(None)) # None value to null

