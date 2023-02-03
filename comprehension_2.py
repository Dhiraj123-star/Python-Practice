# list comprehension (lsit of even number)
even_list = [x for x in range(0,11,2)]
print(even_list)

# (list of odd number by using existing even_list )

odd_list= [ var+1 for var in even_list]
print(odd_list)