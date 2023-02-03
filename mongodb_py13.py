# delete many records 
from pymongo import MongoClient
client=  MongoClient("localhost",27017)
db= client["mydatabase"]
coll=db["myexample1"]

print("Before delete")
for doc in coll.find():print(doc)

coll.delete_many({"age":{"$gt":"26"}}) # delete all the records where age is greater than 26

print("After delete: ")
for doc in coll.find():print(doc)