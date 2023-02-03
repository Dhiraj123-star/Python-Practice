# delete  the table from the database
import psycopg2

# establish the connection 
conn= psycopg2.connect(
    database="mydb",user="postgres",password="mysql",host="localhost",port="5432"
)

# setting the autocommit to False 
conn.autocommit=True
# creating cursor 
cursor = conn.cursor()

# drop the table 
cursor.execute("drop table Employee;")
print("Table dropped successfully!!")

# commit changes
conn.commit()

# close the connection
conn.close()