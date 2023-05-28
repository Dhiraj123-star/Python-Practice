# perform operations on multidimensional array
import numpy as np

arr = np.array([[1,4,5,17],[56,100,77,199],[67,199,198,1090]])

# calculate the sum

print(f"The Total sum is: {np.sum(arr)}")

# calculate the mean 

print(f"the mean of each row: {np.mean(arr,axis=1)}")

# calculate dot product of two matrices

b = np.array([[2,4],[5,6],[7,8],[10,20]])

print(f"The dot product is :  {np.dot(arr,b)}")

