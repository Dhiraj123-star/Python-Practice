# limit the records
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db= client["mydatabase"]
coll= db["myexample1"]

for doc in coll.find().limit(2): print(doc)
