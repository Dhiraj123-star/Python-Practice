# limit  the data from the database
import psycopg2

# establish the connection 
conn= psycopg2.connect(
    database="mydb",user="postgres",password="mysql",host="localhost",port="5432"
)

# setting the autocommit to False 
conn.autocommit=True
# creating cursor 
cursor = conn.cursor()

# retriewing single row 
sql = "select * from Employee Limit 3 offset 1;"

# executing the query
cursor.execute(sql)

# fetching all the data
res= cursor.fetchall()
for i in res: print(i)

# commit the changes 
conn.commit()
# close the connection 
conn.close()