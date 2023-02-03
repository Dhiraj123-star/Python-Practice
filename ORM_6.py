from venv import create
from matplotlib.cbook import strip_math
from sqlalchemy.sql.expression import update 
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String
engine= create_engine("sqlite:///employee.db",echo=True)

meta= MetaData()

employees= Table(
    "Employees",meta,
    Column('id',Integer,primary_key=True),
    Column('name',String),
    Column('age',Integer)

)
conn= engine.connect()
stmt=employees.delete().where(employees.c.age==32) # compare with where
conn.execute(stmt)

e=employees.select() # select the records 

result=conn.execute(e)

for row in result:
    print(row)