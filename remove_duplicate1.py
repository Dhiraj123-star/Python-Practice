# remove the duplicate elements from the list 
def RemoveDuplicate(duplicate):
    mylist=[]
    for i in duplicate:
        if i not in mylist:
            mylist.append(i)
    return mylist

# driver code 
list1=[12,44,55,22,44]
print(RemoveDuplicate(list1))