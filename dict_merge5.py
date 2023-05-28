# merge the dictionaries by |(merge) operator

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

merged_dict = dict1|dict2

pprint(merged_dict)