# file pointer positions
fileptr= open("myfile2.txt","r")

# initially the file pointer is at 0
print("The file pointer is at byte: ",fileptr.tell())

# reading the content of the file
content = fileptr.read()

# seek () modifies the position
fileptr.seek(13) # set to the 13 


print("After seek(),the file pointer is: ",fileptr.tell())