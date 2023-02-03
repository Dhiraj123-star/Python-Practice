# insert the single data 
from pymongo import MongoClient

client = MongoClient("localhost",27017)

# create database instance 
db= client["mydatabase"]

# create collection
col= db["example"]
# insert one data 
data = {"name":"Dhiraj","hobby":"Programming","age":25}

col.insert_one(data)
print("data inserted successfully")