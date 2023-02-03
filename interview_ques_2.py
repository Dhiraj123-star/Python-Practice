# function which takes multiple arguments

def multiple_args(*args):
    for i in args:
        print(i)

# calling the function
multiple_args(9)
multiple_args([12,4,45])
multiple_args(("Java","Python",'JavaScript'))
