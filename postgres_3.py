import psycopg2

# establish the connection 
conn= psycopg2.connect(
    database="mydb",user="postgres",password="mysql",host="localhost",port="5432"
)

# setting auto commit false 
conn.autocommit=False

# creating cursor object
cursor = conn.cursor()

# preparing SQL Queries to insert 

Sql= ''' Insert into Employee(First_name,Last_name,Age,Gender,Income)
               Values('Ramya','Rama Priya', 27, 'F', 9000 ),
               ('Vinay','Battacharya', 20,'M',9100),
               ('Sharukh', 'Sheik', 25,'M', 8900),
               ('Sarmista','Sharma', 26,'F', 10000),
               ('Triputi', 'Mishra', 34,'F', 7650);'''

# execute the query
cursor.execute(Sql)

# commit the changes
conn.commit()

print("Records added successfully")
# close the connection
conn.close()

