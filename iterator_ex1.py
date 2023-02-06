# iterator in Python
# There are some objects(List,Tuple and Dictionary) are iterable
# which means we can traverse over them and they will return
# their member value one by one

my_secret = ["I", "Love","Python"]

myiter = iter(my_secret)
print(myiter)
print(next(myiter))
print(next(myiter))
print(next(myiter))