# set comprehension using set

even_set = {x for x in range(0,11,2)} # stores the even numbers in the set
print(even_set)
odd_set = {var+1 for var in even_set}
print(odd_set)