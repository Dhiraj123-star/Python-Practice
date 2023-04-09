import copy 

original_list = [12,34,[10,23]]

shallow_copy = copy.copy(original_list)

# modify the list 
original_list[2][1]=100

print(original_list) # both the lists got changed 
print(shallow_copy)

# deep copy 

deep_copy = copy.deepcopy(original_list)
# modify the list
original_list[2][1]=1000

print(original_list)
print(deep_copy) # deep copy remains unchanged but original list is changed 