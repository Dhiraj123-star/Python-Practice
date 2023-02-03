# arrays store heterogeneous data when imported from the array module
# but arrays can store homogeneous data when imported from numpy module

import array as ar
import numpy as np
array1 = ar.array('i',[12,45,905]) 
print(array1)
array2= np.array([12,45,78,"Str"]) # it keeps the data type is same throughout the array
print(array2)