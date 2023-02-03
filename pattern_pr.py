# number pattern program in Python
for i in range(1,9):
    for j in range(1,i):
        print(j,end=" ")
    print() # for new line 

# # pattern 

print() # for new line

for i in range(1,10):
    for j in range(1,i):
        print("#",end=" ")
    print() # for new line 

print() # for new line

currentnum= 1
stop=2
rows=3

for i in range(rows):
    for column in range(1,stop):
        print(currentnum,end=" ")
        currentnum+=1
    print(" ")
    stop+=2


