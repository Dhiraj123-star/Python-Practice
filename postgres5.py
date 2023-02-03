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

# populating the table 

insert_stmt = """Insert into Employee (First_name,Last_name,Age,Gender,Income)
                Values(%s,%s,%s,%s,%s)"""
data= [('Krishna','Sharma',19,'M',2000),
        ('Raj','Kandukari',20,'M',9000),
        ('Ramya','Agarwal',35,'F',10001),
        ('Mac','Mohan',26,'M',20000)]
cursor.executemany(insert_stmt,data)

# retriewing specific records using the where clause 
cursor.execute("Select * from Employee where Gender='F';")

result = cursor.fetchall()

for i in result:print(i)

# commit the changes
conn.commit()
# close the connection
conn.close()