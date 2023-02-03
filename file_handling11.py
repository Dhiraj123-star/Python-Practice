# readline() function
fileptr= open("myfile2.txt","r")
# stores all the data of the file into variable content
content= fileptr.readline()
content1=fileptr.readline()
# prints the content of the file
print(content)
print(content1)
# close the file
fileptr.close()