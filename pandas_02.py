import numpy as np
import pandas as pd

emp_details = {
    'name':['Bill','Mark','Elon','Jack'],
    'Company':['Microsoft','Facebook','Tesla','Alibaba'],
    'age':[65,44,45,50]
}

df = pd.DataFrame (emp_details)
print("The top : ")
print(df.head(3) )

print("From bottom: ")
print(df.tail(2))

print(df.describe()) # it calculates some statistical data like percentage,mean like this.

print("Read data from csv: ")
read = pd.read_csv("Dhiraj.csv")

print(read)

print("Read only name: ")
print(read["name"])

print("Read only company: ")
print(read["Company"])

