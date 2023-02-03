# remove duplicate elements from list using operator
import operator as op

def RemoveDuplicate(duplicate):
    final_list=[]
    for i in duplicate:
        if op.countOf(final_list,i)==0:
            final_list.append(i)
    return final_list

# driver code
list1=[12,34,12,34,100]
print(RemoveDuplicate(list1))
