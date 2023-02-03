# python program to construct a calculate the
#  means of the numbers in the list
n= int(input("Enter the number of element to take average of: "))
l=[] # empty list

for i in range(n):
    element = int(input("Enter your element: "))
    l.append(element)

avg = sum(l)/n # here we calculate the mean of the list's elements

print("The average is: ",avg)
