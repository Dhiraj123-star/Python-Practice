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

# retriewing specific records using the order by 
cursor.execute("select * from Employee order by age desc;")
result = cursor.fetchall()
for i in result:
    print(i)

# close the connection
conn.close()