# update with update() method 
from pprint import pprint
dict1 = {
    "name":"Rahul",
    "age":34,
    "hobby":"Python Programming"
}

dict2  = {
    "interest":"Coding"
}

# merge the two dictionaries with update () 

dict1.update(dict2)

pprint(dict1)
