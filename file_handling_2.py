# file read () function
with open("myfile.txt","r") as f:
    print("First 4 lines of the file: ",f.read(4))
    print(f.read()) # another contents except first 4 lines

    

