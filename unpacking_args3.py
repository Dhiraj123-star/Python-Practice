# more example on packing and unpacking

def print_eligiblity(name,age,eligibility):
    print(f'Hey {name}, you are {eligibility} to vote')

def check_eligibility(*args):
    # convert args tuple to a list so we can modify it
    args=list(args)
    if args[1]>=18:
        elig= "Eligible"
    else:
        elig="not eligible"
    args.append(elig)
    print_eligiblity(*args)

# driver code 

name = input("Enter your name: ")
age= int(input("Enter your age: "))
check_eligibility(name,age)