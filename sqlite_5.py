import sqlite3
conn= sqlite3.connect("test.db")
print("Database opened successfully")

conn.execute("UPDATE Company SET SALARY=90000 WHERE ID=1;")
conn.commit()
print("Total number of rows updated",conn.total_changes)

cursor = conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY From Company;")

for row in cursor:
    print("ID: ",row[0])
    print("NAME: ",row[1])
    print("AGE: ",row[2])
    print("ADDRESS: ",row[3])
    print("SALARY: ",row[4])

print("Operation done successfully")
conn.close() # closing connection
