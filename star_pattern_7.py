# diamond shaped pattern 

rows = int(input("Enter no. of rows: "))

m = (2*rows)-2

# outer loop to print no.of rows 
for i in range(0, rows):
    # inner loop is used to print no. of space 
    for j in range(0,m):
        print(end=" ")

    # decrement in k after each iteration
    m=m-1

    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")


m= rows-2 

for i in range(rows,-1,-1):
    for j in range(m,0,-1):
        print(end= " ")
    m+=1

    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")