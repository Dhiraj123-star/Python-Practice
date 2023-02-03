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
# fetching all the rows before the update 

print("Contents of the Employee before update")
sql='''select * from Employee;'''
cursor.execute(sql)
result = cursor.fetchall()
for i in result:
    print(i)

# updating the records
sql = "update Employee set Age= Age+1 Where Gender='M';"
cursor.execute(sql)
print("Table updated...")
# fetching the records
print("Contents of the Employee table after updation")
sql="Select * from Employee;"
cursor.execute(sql)
myresult= cursor.fetchall()
for i in myresult:
    print(i)

# commit all the changes 
conn.commit()
# close the connection
conn.close()