# update single record  in collection
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db= client["mydatabase"]
coll= db["myexample1"]

coll.update_one({"_id":"1002"},{"$set":{"city":"Visakshapatnam"}})

print("After Update :")
for doc in coll.find():print(doc)