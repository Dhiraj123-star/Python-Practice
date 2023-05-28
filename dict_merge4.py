# merge the dictionaries with chainmap

from collections import ChainMap
from pprint  import pprint

dict1={
    "name":"Python",
    "rank":1,
    "Framework":"Django"
}

dict2 = {
   "Libraries":"Numpy",
   "Resources":"FreeCodeCamp"
}

# merge the dictionaries

merged_dict = dict(ChainMap(dict1,dict2))


pprint(merged_dict)