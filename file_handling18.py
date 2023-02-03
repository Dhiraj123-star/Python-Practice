# picking
# it is used for serialising and de-serialising python
# object structures
import pickle
mylist = ["a","b","c","d"]

with open("datafile.txt","wb") as file:
    pickle.dump(mylist,file)

print("File dumped successfully!!")