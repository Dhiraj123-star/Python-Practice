# defaultDict 
# it provides some default values for the key that doesnot exist
# never raises the keyError

from collections import defaultdict

# defining the defaultDict
d = defaultdict(int)

L=[1,2,3,4,1,2,4,3]

# iterate through the list for keeping the count 

for i in L:
    d[i]+=1

print(d)