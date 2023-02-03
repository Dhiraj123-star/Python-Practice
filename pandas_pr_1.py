# create a new column in pandas by using values from other columns 
import pandas as pd 
a=[1,2,3]
b=[4,8,9]
d={"col1":a,"col2":b}
df=pd.DataFrame(d)
df["Sum"]=df["col1"]+df["col2"]
df["subtract"]=df["col1"] - df["col2"]
print(df)