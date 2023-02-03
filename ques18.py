# reverse the given list
mylist =[12,45,450,90]
mylist.reverse() 
print("Using reverse() function: ",mylist)

print("using for loop: ")
for i in range(len(mylist)-1,-1,-1):
    print(mylist[i],end=" ")

    