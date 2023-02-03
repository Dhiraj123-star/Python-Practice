# select the data from the database
import psycopg2

# establish the connection 
conn= psycopg2.connect(
    database="mydb",user="postgres",password="mysql",host="localhost",port="5432"
)

# setting the autocommit to False 
conn.autocommit=False
# creating cursor 
cursor = conn.cursor()

# retrieving the data
cursor.execute('''select * from Employee;''')

# fetching 1st row from the table 
result = cursor.fetchone() 
print(result)

#  fetching many data 

myresult = cursor.fetchall()

for i in myresult:
    print(i)
# commit the changes 
conn.commit()
# close the connection
conn.close()