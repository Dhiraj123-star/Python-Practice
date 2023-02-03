# remove the duplicate element from the list using list comprehension 
list1=[1,3,4,6,1,3,2]

new_list=[list1[i] for i in range(len(list1))if list1.index(list1[i])==i]

print(new_list)

