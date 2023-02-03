# generator comprehension using python
even_list = [x for x in range(0,15,2)]
print(even_list)
odd_list = (var+1 for var in even_list) # generator 

for myvar in odd_list:
    print(myvar,end=" ")

