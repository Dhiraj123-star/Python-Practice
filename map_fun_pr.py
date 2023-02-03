def add(n):
    return n+n 

numbers=[12,34,33,45]
res= map(add,numbers)
print(list(res)) # convert into the list to get output otherwise it returns map object 

# for tuple
def subme(n):
    return n-n

nums =(90,100,22)

res1 = map(subme,nums)
print(tuple(res1))
