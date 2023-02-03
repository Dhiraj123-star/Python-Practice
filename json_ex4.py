# deserialisation is the process of conversion of JSON objects into their 
# respective objects
import json

with open("Sample.json","r") as readfile:
    data = json.load(readfile) # deserialise 

print(data)