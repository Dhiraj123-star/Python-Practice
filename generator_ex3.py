# difference between list comprehension and generator comprehension
# in list comprehension there is square bracket used whereas in generator
# comprehension uses round bracket

list1 = [12,45,450,90,100]

mylist= [x**2 for  x in list1]
print(mylist)

mygen = (x**2 for x in list1)

print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
print(next(mygen))
# print(next(mygen)) # Stop Iteration error 