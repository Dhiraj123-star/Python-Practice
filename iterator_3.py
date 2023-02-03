from itertools import count

# create an infinite iterator that starts at 1 and 
# increments by one 

infinite_iterator = count(1)

for i in range(5):
    print(next(infinite_iterator))