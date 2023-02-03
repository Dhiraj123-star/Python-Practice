# open file "myfile.txt" in read mode
fileptr= open("myfile.txt","r")
if fileptr:
    print("file opened successfully!!")

# close the file
fileptr.close()
