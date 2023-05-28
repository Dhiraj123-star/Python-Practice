# merge the dictionaries with (**) double asterick 

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

# merge the dict

merge_dict = {**dict1 , **dict2} # key names should be different , if same it gets replaced by new one

pprint(merge_dict)


devBio = {
  "name": "Ihechikara",
  "age": 500,
  "language": "Python"
}

tools = {
  "dev environment": "JupyterLab",
  "os": "Windows",
  "visualization": "Matplotlib"
}

merged_bio = { **devBio, **tools}

print() # for new line
pprint(merged_bio)