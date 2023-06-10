'''
JSONEncoder class allows you to customize the encoding process. 
To define how your custom object should be encoded into JSON format, 
you can extend the JSONEncoder and change its default method.

'''

import json

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,Person):
            return {"name":obj.name,"age":obj.age}
        return super().default(obj)

# create a custom object
person = Person("Krishna",23)

# encode the custom object using the custom encoder

json_str = json.dumps(person,cls=PersonEncoder)

print(json_str)