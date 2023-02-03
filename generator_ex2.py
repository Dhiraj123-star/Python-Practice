# generator function to yield multiple statements
def mygen():
    str1 = "Python Programming"
    yield str1
    str2 = "Java Programming"
    yield str2
    str3 = "JavaScript Programming"
    yield str3

# create a generator object
obj = mygen()
print(next(obj))
print(next(obj))
print(next(obj))
#print(next(obj)) # returns StopIteration Error