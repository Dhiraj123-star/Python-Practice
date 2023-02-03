import sqlite3
conn= sqlite3.connect("test.db")
print("Database opened successfully")

# insert the values into the table
conn.execute("INSERT INTO Company(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(1,'Dhiraj',23,'Bhiwadi',780000)");

conn.execute("INSERT INTO Company(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(2,'Dhawan',26,'Khanna',790000)");

conn.execute("INSERT INTO Company(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(3,'Pratham',13,'Gurgaon',80000)");

conn.execute("INSERT INTO Company(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(4,'Prashant',28,'NOIDA',70000)");

conn.execute("INSERT INTO Company(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(5,'Dhruv',30,'Gandhinagar',810000)");

conn.execute("INSERT INTO Company(ID,NAME,AGE,ADDRESS,SALARY)\
            VALUES(6,'Rakesh',29,'Rewari',90000)");

conn.commit() # commit the data

print("Records added successfully in the database")

conn.close() # close the connection

