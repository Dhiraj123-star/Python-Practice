# delete single record 
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db= client["mydatabase"]
coll= db["myexample1"]

print("Before delete")
for doc in coll.find():print(doc)

coll.delete_one({"_id":"1002"})

print("After delete: ")
for doc in coll.find():print(doc)