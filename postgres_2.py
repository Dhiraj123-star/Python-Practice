# create table 
import psycopg2

# establish the connection 
conn= psycopg2.connect(
    database="mydb",user="postgres",password="mysql",host="localhost",port="5432"
)
# creating cursor 
cursor= conn.cursor()
# droping table if already exists
cursor.execute("Drop table if exists Employee;")

# creating table 
sql = '''
        Create table Employee (
            First_name char(20) not null,
            Last_name char(20) not null,
            Age INT,
            Gender Char(1),
            Income FLOAT);
            '''
cursor.execute(sql)
print("Table created Successfully")
conn.commit() # commit the changes 
# closing the connection
conn.close()