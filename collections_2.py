# orderedDict

from collections import OrderedDict

print("This is a Dict")

d={} # empty dictionary 
d[1]="Python"
d[2]="Java"
d[3]="C"
d[4]="C++"

for key,value in d.items():
    print(key,value)

print("This is orderedDict")
od=OrderedDict()
od["Python"]=1
od["Java"]=2
od["C"]=3
od["C++"]=4

print("Before Deleting ")
for key,value in od.items():
    print(key,value)

# deleting the item 
od.pop("Python")
# re-inserting the value 

od["Python"]=5

print("After re-inserting ")
for key,value in od.items():
    print(key,value)