# picking the dictionary 
import pickle

EmpId ={1:"Zack","age":34,"hobby":"Programming"}

picking_one= open("EmpId.pickle","wb")
pickle.dump(EmpId,picking_one)

picking_one.close() 
print("file contents saved!!")
