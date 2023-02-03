# star pattern in Python 

rows = int(input("Enter no. of rows: "))

for i in range (1, rows+1):
    for j in range (1, i+1):
        print("*",end=" ")
    print()

for i in range(rows+1,1,-1):
    for j in range(i+1,1,-1):
        print("*",end= " ")
    print()