# create json object from dictionary 

import json

# python dictionary

data = {
    "Name":"Python",
    "Rank":1,
    "Type":"Interpreted Programming Language"
}

# convert into json

json_str = json.dumps(data,indent=4)

print(json_str)



