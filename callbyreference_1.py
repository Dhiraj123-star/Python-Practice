# print the address of the list before calling the function
# after calling the function

def myfun(mylist):
    print("List received ",mylist)
    mylist.append(3)
    mylist.extend([45,90])
    print("List after adding some elements ",mylist)
    mylist.remove(90)
    print("Address within function ")
    print(id(mylist))
    print("List within called function ",mylist )
    return

list1=[1]
print("Address before calling ",id(list1))
print("List before function call ",list1)
myfun(list1)
print("List after function call ",list1)
print("Address after calling ",id(list1))