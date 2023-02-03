# create collection 
from pymongo import MongoClient

client = MongoClient("localhost",27017)

# getting the database instance 
db=client["mydatabase"]
# create collection
collection = db["example"]
print("Collection created...")
