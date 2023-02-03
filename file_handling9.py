# read the file contents 
fileptr= open("myfile2.txt","r")

content= fileptr.read(13) # read first 13 lines of the code
# print the type of contents
print(type(content))
# print the contents of the file
print(content)
# read the whole content
print(fileptr.read())
# close the file
fileptr.close()