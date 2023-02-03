# file handling with for loop 
with open("myfile.txt","r") as f:
    for i in f.read():
        print(i)
        