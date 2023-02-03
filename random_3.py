# random.choice() selects an item from a non-empty series at random.
import random
random_s = random.choice("Random Module") # string
print("The random choice in string: ",random_s)

random_I = random.choice([12,56,90,100,345]) # list 
print("The random choice in integer: ",random_I)

random_set = random.choice((90,45,90,45,100)) # set
print("The random choice in set: ",random_set) 