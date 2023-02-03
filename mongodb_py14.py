# drop the collection
from pymongo import MongoClient
client= MongoClient("localhost",27017)
db= client["mydatabase"]
coll=db["myexample1"]

print("Total collections before drop: ")
collections = db.list_collection_names()
for i in collections:print(i)

coll.drop()

print("Total collections after drop: ")
collections=db.list_collection_names()
for i in collections:print(i)
