# write a program for a table using generator
def mytable(n):
    for i in range(1,11):
        yield n*i
    
# call the function
for i in mytable(12):
    print(i)