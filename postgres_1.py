# creating a database in postgresql using Python

import psycopg2

# establish the connection 
conn= psycopg2.connect(
    database="postgres",user="postgres",password="mysql",host="localhost",port="5432"
)

conn.autocommit=True # to set the commit to True value 

cursor = conn.cursor() # create the cursor object 

# preparing the query to create a database 
sql = '''Create database mydb;'''

# creating the database

cursor.execute(sql)

print("Database created successfully!!")

# close the connection
conn.close()

