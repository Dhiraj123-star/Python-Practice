# reduce function
from functools import reduce

numbers = [1,23,56,78,100]

reduce_num = reduce(lambda x,y:x+y,numbers)

print(reduce_num)
