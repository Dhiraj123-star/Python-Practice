# modify and access multidimensional array 

import numpy as np

arr = np.array([[13,45,56,100],[12,67,33,101],[78,88,90,900]])

print(arr)

print(f"The accessed element: {arr[2,2]}") # 90 

# modify 

arr[1,3]=1000

print("After modified:\n",arr)

