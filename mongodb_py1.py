# create a database using python in mongodb
from pymongo import MongoClient

# create  a pymongo Client
client= MongoClient("localhost",27017)

# Getting the database instance
db=client['mydatabase']

print("Database created...")

# verify the database 
print("List of the database: ",client.list_database_names())