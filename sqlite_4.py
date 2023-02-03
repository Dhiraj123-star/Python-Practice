import sqlite3
conn= sqlite3.connect("test.db")
print("Database opened successfully")

cursor = conn.execute("Select ID,NAME,AGE,ADDRESS,SALARY from Company;")

for row in cursor:
    print ("ID: ",row[0])
    print("NAME: ",row[1])
    print("AGE: ",row[2])
    print("ADDRESS: ",row[3])
    print("SALARY: ",row[4])

print("operation done successfully")

conn.close() # close the connection