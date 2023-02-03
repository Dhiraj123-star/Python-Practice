# find the records of collections 
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db= client["mydatabase"]
coll= db["myexample"]


#Retrieving all the records using the find() method
print("Records of the collection: ")
for doc1 in coll.find():
    print(doc1)

#Retrieving records with age greater than 26 using the find() method
print("Record whose age is more than 24: ")
res=coll.find({"age":{"$gt":"24"}})
for doc2 in res:
    print(doc2)