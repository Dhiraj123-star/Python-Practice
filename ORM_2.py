from sqlalchemy import create_engine, MetaData,Table,Column, Integer,String

engine = create_engine("sqlite:///employee.db",echo=True)
meta = MetaData()

employees = Table(
    'Employees',meta ,
    Column('id',Integer,primary_key=True),
    Column('name',String),
    Column('age',Integer)
)
meta.create_all(engine)

print("Table created successfully")

# insert values into the table
ins = employees.insert()
ins= employees.insert().values(id=1,name="Rahul",age=32)
conn = engine.connect()
result= conn.execute(ins)