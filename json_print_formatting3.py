# using third-party libraries
"""

There are many third-party libraries available in Python
for pretty printing JSON data, such as simplejson, ujson, and json5.
These libraries provide additional features such as faster serialization and
deserialization, support 
for additional data types, and more flexible formatting options

"""
import simplejson as json

data ={

    "name":"Python",
    "rank":1,
    "type":"Interpreted-Programming"
}

json_str = json.dumps(data,indent=4,sort_keys=True)

print(json_str)