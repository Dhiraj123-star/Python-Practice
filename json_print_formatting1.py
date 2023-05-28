import json
data = {
    "name":"john",
    "age":30,
    "place":"Dubai"
}

json_str = json.dumps(data,indent=4) # formatting with indent parameter 
# which gives 4 space identation

print(json_str)