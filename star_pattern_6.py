# printing downward triangle

rows = int(input("Enter no. of rows: "))

m= (2*rows)-2 
# outer loop in reverse order 

for i in range(rows,-1,-1):
     
     # inner loop will print the number of spaces 
    for j in range(m,0,-1):
        print(end= " ")
    
    m+=1

    for j in range(0,i+1):
        print("*",end=" ")
    

    print("")