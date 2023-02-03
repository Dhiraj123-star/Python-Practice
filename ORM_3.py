from sqlalchemy import create_engine, MetaData,Table,Column, Integer,String

engine = create_engine("sqlite:///Students.db",echo=True)
meta = MetaData()

Students = Table(
    'Students',meta ,
    Column('id',Integer,primary_key=True),
    Column('name',String),
    Column('age',Integer)
)
meta.create_all(engine)

conn=engine.connect()

# insert multiple values 
conn.execute(Students.insert(),[
    {'name':'Rajiv','age':32},
    {'name':'Komal','age':23},
    {'name':'Roshani','age':30},
    {'name':'Abdul','age':40}

])

print("data inserted successfully")

