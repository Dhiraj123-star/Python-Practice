# unpacking the arguments in Python

values =(1,2,4,5,9)

def add_numbers(*args):
    total =0
    for i in args:
        total+=i
    print(total)
    return total

# driver code 
add_numbers(*values) # here we unpacking the args


# another example

details = ("1","Aryan","Computer Science")

def func(id,name,subject):
    print(f"Roll number {id} is {name} from {subject}")

# driver code

func(*details) # here we have to aware that we should pass as same as 
# we define in the function like in func (there is 3 arguments so we have to pass only 3.
# otherwise we got an error)
