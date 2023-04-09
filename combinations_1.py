# combination in Python
import itertools
letters = ['a','b','c','d']

combinations =[]

# generate combinations of length 2 

for combination  in itertools.combinations(letters,3):
    combinations.append(combination)

print(combinations)