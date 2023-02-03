# remove the elements from the list using defaultdict
from collections import defaultdict

def default_val(): 
    return 0

# dict: maintain count of each element. with default value of key is 0
mydict= defaultdict(default_val)

# list with duplicate values 
l=[90,90,80,76,45,90]

for i in l:
    # if element is already present then remove the element 
    if mydict[i]==1:
        l.remove(i)
    else:
        mydict[i]=1
# printing the final array
print(l)

