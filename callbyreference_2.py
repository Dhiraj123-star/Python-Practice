# change is not referenced outside the function

def myfun(mylist):
    print("List received ",mylist)
    mylist.append(3)
    mylist.extend([10,20])
    print("List after adding some elements ",mylist)
    mylist.remove(20)
    mylist=[90,100]
    print("Address within the function ",id(mylist))
    print("List within the called function ",mylist)

list1=[1]
print("Address before calling ",id(list1))
print("List before calling function ",list1)
myfun(list1)
print("List after function call ",list1)
print("Address after function call ",id(list1))

