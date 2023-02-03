# sort the records in collection
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db= client["mydatabase"]
coll= db["myexample1"]

# sort the age by ascending
for i in coll.find().sort("age"):print(i)
