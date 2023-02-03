# remove the duplicate from the list using set
def RemoveDuplicate(duplicate):
    new_list=[]
    for i in set(duplicate):
        new_list.append(i)
    return new_list

# driver code
list1= [12,45,67,12]
print(RemoveDuplicate(list1))
