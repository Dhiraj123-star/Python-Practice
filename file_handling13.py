# file pointer positions
fileptr= open("myfile2.txt","r")

# initially the file pointer is at 0
print("The file pointer is at byte: ",fileptr.tell())

# reading the content of the file
content = fileptr.read()

# after read operation
# file pointer modifies the tell()

print("After reading,the file pointer is: ",fileptr.tell())