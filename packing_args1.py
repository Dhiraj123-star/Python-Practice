# packing with * operator

# all arguments passed to func are packed into tuple *args
def func(*args):
    # accessing the elements just like we access then from a tuple
    print(args[0])

    # convert args tuple to a list so we can modify it
    args = list(args)

    # modifying args 
    args[0]= "Python"
    args[1]= "Programming"
    print(args)

# driver code 
func("Java", "Programming")

# another function

def add_numbers(*args):
    total =0
    for i in args:
        total+=i
    return total

# driver code 
print(add_numbers(12,33))
print(add_numbers(12,89,19))

