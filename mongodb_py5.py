# find the records of collections 
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db= client["mydatabase"]
col= db["myexample"]

print("First record of collection: ")
print(col.find_one())

print("Find multiple records: ")
records= col.find()
for i in records:
    print(i)
print("records where age is greater than 24: ")
myrecord = col.find({"age":{"$gt":"24"}})

for i in myrecord:
    print(i)