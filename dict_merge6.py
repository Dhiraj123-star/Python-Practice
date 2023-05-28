# merge the dictionaries by |=(update) operator 
from pprint import pprint 
dict1 = {
    "name":"Python",
    "rank":1,
    "Framework":"Django"
}

dict2 = {
   "Libraries":"Numpy",
   "Resources":"FreeCodeCamp"
}


dict1|=dict2

pprint(dict1)