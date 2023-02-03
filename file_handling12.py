# readlines() function in Python
fileptr=open("myfile2.txt","r")
# stores all the data of the file into the variable
content = fileptr.readlines()

print(content)
#close the file
fileptr.close()