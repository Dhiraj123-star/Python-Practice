# call by reference 
# it is a way of passing arguments to a function call in which both the
# actual argument and formal parameters refer to the same memory locations
# and any changes made within the reflected in the actual paramters of
# the function when called 

# call by reference example

def myfun(mylist):
    print("List received ",mylist)
    mylist.append(3)
    mylist.extend([10,30])
    print("List after adding some elements ",mylist)
    mylist.remove(10)
    print("List within function call ",mylist)
    return

List1=[1]
print("List before calling the function ",List1)
myfun(List1)
print("List after function call ",List1)
