# file handling 
fileptr= open("myfile2.txt","w")

# appending the contents in the file
fileptr.write("Python is the modern day language.It makes things so simple.\
            It is the fastest growing programming language ")

# closing the file
fileptr.close()
print("File contents written successfully!!")