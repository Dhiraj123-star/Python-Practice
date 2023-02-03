# append the contents in the file
with open("myfile.txt","a") as f:
    f.write(" This content is added at the last")

print("read contents of the file: ")
with open("myfile.txt","r") as f:
    print(f.read())
