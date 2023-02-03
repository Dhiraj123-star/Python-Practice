# append the contents 
fileptr= open("myfile2.txt","a")

# overwriting the content of the file
fileptr.write("Python has an easy syntax and user-friendly interaction")

# closing the file
fileptr.close()
print("Contents appended successfully!!")