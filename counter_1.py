# counter in Python
from collections import Counter

numbers = [1,2,3,1,3,4,5,6,5,4,3,2,1,2]

counter = Counter(numbers)

print(counter[3]) # it returns count of 3 

print(counter)