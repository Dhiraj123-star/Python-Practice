# insert multiple data 
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db= client["mydatabase"]
col= db["myexample"]
data1=[
    {"name":"Pratham","age":21,"hobby":"teaching"},
    {"name":"Komal","age":24,"hobby":"Reading"},
    {"name":"Nisha","age":43,"hobby":"cooking"}
]
# insert many data
col.insert_many(data1)
print("Data inserted successfully")