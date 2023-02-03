# update the many records in collection
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db= client["mydatabase"]
coll= db["myexample1"]

print("Before Update: ")
for doc in coll.find():print(doc)

coll.update_many({},{"$set":{"city":"Bhiwadi"}})
print("After Update: ")
for doc in coll.find():print(doc)
