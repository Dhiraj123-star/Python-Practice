# list comprehension in python
blue_list = ["blue","blue","blue","blue"]
print(blue_list)
red_list=[] # empty list 
for i in blue_list:
    red_list.append("red")

print(red_list)

print("Using list comprehension")

mylist = ["red" for _ in blue_list]

print(mylist)