# hour glass in Python 

rows = int(input("Enter no. of rows: "))

k= rows-2

# this is used to print the downward pyramid 
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")

    k+=1
    for j in range(0,i+1):
        print("* ",end="")
    print()

# this is used to print the upward pyramid 

k = (2*rows)-2

for i  in range(0, rows+1):
    for j in  range(0,k):
        print(end=" ")

    k-=1

    for j in range(0,i+1):
        print("* ",end="")

    print()



