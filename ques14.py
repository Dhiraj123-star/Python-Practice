# python array 
import array as arr

myarray = arr.array("i",[1])

# add single element 
myarray.append(100) 
print(myarray)
# extend the array with multiple values 
myarray.extend([12,101,200])
print(myarray)
# insert at the specific position
myarray.insert(3,1000)
print(myarray)

# remove the element 

print("Remove operation: ")

print(myarray.pop()) # remove the last position element 
print(myarray.pop(2)) # remove the second position element
myarray.remove(1) # remove 1(it takes removed value) from the array 
print(myarray)
