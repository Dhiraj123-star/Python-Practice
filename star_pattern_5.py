# printing Triangle Pyramid 

rows = int(input("Enter no. of rows: "))

m= (2*rows)-2 

for i in range(0,rows):
    for j in range(0,m):
        print(end=" ")
    m=m-1 # decrementing m after each loop

    for j in range(0,i+1):
        # printing full triangle pyramid using stars 
        print("*" , end= " ")

    print(" ")
