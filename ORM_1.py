# ORM using sqlalchemy 
from sqlalchemy import create_engine #for sqlite3 
create_engine("sqlite:///college.db",echo=True)

print("Database created successfully!!")