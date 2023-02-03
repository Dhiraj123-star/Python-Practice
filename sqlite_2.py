import sqlite3
conn=sqlite3.connect("test.db")
print("opened database successfully")

# create table 
conn.execute('''Create table Company (ID INT PRIMARY KEY  NOT NULL, 
            NAME  TEXT NOT NULL,
            AGE INT NOT NULL,
            ADDRESS CHAR(50), 
            SALARY REAL);''')

print("Table created successfully")

conn.close() # closing the connection