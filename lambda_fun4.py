# use of Python lambda function inside the reduce () function
from functools import reduce


numbers = [12,56,89,100,13]

# one liner code to do the addition of all numbers using reduce() function 

red_numbers= reduce((lambda x,y:x+y),numbers)


print(red_numbers)


