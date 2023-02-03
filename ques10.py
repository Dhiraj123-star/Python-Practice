# list,set and dictionary comprehension

list_comp = [i for i in range(3)]
print(list_comp)
print(type(list_comp))

dict_comp = {i:i**2 for i in range(3)}
print(dict_comp)
print(type(dict_comp))

set_comp = {i for i in range(3)}
print(set_comp)
print(type(set_comp))
