# query in collection
from pymongo import MongoClient
client = MongoClient("localhost",27017)
db= client["mydatabase"]
coll=db["myexample"]

# find the particular name in collection
res= coll.find({"name":"Pratham"})
for i in res: print(i)
# find age is less than 30
res1 =coll.find({"age":{"$lt":"30"}})
for j in res1:print(j)