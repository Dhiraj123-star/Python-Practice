# merge the dictionaries with chain()

from itertools import chain
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

# merge the dictionaries

merge_dict  = dict(chain(dict1.items(), dict2.items()))

pprint(merge_dict)