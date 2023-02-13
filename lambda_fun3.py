# use of the python lambda function inside the map() function

numbers = [12,5,8,9,10]

# one liner code to create the list of squares of the numbers using map() function

sq_numbers = list(map((lambda x:x**2),numbers))

print(sq_numbers)


