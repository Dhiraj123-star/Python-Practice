# numpy example 
import numpy as np
import pandas as pd

# dictionary of lists
dict={
    "id":[1,4,np.nan,67],
    "age":[np.nan,56,43,np.nan],
    "Score":[678,56,np.nan,5]

}

# creating the dataframe
df =pd.DataFrame(dict)

print(df.isnull().sum())