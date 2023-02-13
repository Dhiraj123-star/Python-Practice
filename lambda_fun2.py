# use of the python lambda function inside the filter()function

numbers= [12,5,7,8,9,11]

# one liner code to make list of even numbers using filter() function

even_no = list(filter((lambda x:x%2==0  ),numbers))

print(even_no)

