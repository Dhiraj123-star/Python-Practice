# remove elements from list using counter 
from collections import Counter

# list 
list1=[12,45,12,89,45]
unique = Counter(list1)
print(unique.keys())

