# unpicking the dictionary
import pickle
pickle_off = open("EmpId.pickle","rb")
EMP= pickle.load(pickle_off)
print(EMP)