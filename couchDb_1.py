# importing couchdb

import couchdb
couch = couchdb.Server() # connecting with couchdb Server 

# creating database 

db= couch.create('MyDatabase')
print("Database Created")

# creating document 
doc = {"name":"Dhiraj Kumar", "age":25,
       "hobby": "Programming"}
    
db.save(doc) # saving the document
print("Document created")

#fetching document from the database 

print("Name is: ",doc['name'])
