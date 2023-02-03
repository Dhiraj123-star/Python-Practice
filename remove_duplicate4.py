# remove the duplicate value from the list using fromkeys() method

list1= [12,4,4,12,8]

mylist= list(dict.fromkeys(list1))
print(mylist)