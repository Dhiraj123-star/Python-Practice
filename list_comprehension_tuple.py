# list comprehension with tuple 

names = ["Alex","James","John","Hales"]
age = [13,45,77,44]

person_info =[(name,age) for name ,age in zip(names,age) ]
print(person_info)