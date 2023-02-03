# program for print simple reversed right angle pyramid pattern 

rows = int(input("Enter the number of rows: "))

k =  2*rows -2 # it is used for number of spaces

for i in range( rows):
    for j in range(k):
        print(end=" ")
    k= k-2 # decrement k value after each iteration

    for j in range (i+1):
        print (" * ",end= " ")
    print(" ")