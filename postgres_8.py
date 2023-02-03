# update the data from the database
import psycopg2

# establish the connection 
conn= psycopg2.connect(
    database="mydb",user="postgres",password="mysql",host="localhost",port="5432"
)

# setting the autocommit to False 
conn.autocommit=True
# creating cursor 
cursor = conn.cursor()

# retriewing the contents of the table
print("Contents of the table-----")
cursor.execute('Select * from Employee;')
result =cursor.fetchall()
for i in result: print(i)

# delete the records where age is less than 25
cursor.execute("Delete from Employee where first_name='Ramya';")

# retrieving data after delete
print("Contents after delete operation")
cursor.execute('Select * from Employee;')
res= cursor.fetchall()
for i in res:
    print(i)

# commit the changes
conn.commit()
# close the connection
conn.close()
