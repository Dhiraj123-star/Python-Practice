from sqlalchemy import Column, create_engine,MetaData,String,Integer,Table,ForeignKey
from sqlalchemy.sql import select
engine = create_engine("sqlite:///college.db",echo=True)
meta = MetaData()
# first Table (students)
students= Table(
    'students',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String),
    Column('lastname',String)
)
# second table(addresses)
addresses = Table(
    'addresses',meta,
    Column('id',Integer,primary_key=True),
    Column('st_id',Integer,ForeignKey('students.id')),
    Column('postal_add',String),
    Column('email_id',String)
)
conn= engine.connect()
s= select([students,addresses]).where(students.c.id==addresses.c.st_id)

result = conn.execute(s)

for row in result:
    print(row)