# unpicking 
# we can convert the byte-stream into python objects

import pickle
pickle_off= open("datafile.txt","rb")

data = pickle.load(pickle_off)
print(data)