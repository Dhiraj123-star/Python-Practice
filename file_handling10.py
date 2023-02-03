# read the contents using for loop
fileptr= open("myfile2.txt","r")
# running a for loop
for i in fileptr:
    print(i)
# close the file 
fileptr.close()