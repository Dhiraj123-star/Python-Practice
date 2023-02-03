import pandas as pd
import numpy as np

emp_details = {
    'name':['Bill','Mark','Elon','Jack'],
    'Company':['Microsoft','Facebook','Tesla','Alibaba'],
    'age':[65,44,45,50]
}
df= pd.DataFrame(emp_details)
print(df)
df.to_csv("Dhiraj.csv")
print("File saved successfully!!")