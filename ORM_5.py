from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String
engine= create_engine("sqlite:///employee.db",echo=True)
meta = MetaData()
employees = Table(
    'Employees',meta ,
    Column('id',Integer,primary_key=True),
    Column('name',String),
    Column('age',Integer)
)
conn= engine.connect()
stmt= employees.update().where(employees.c.name=="Rahul").values(name="Mohit")
conn.execute(stmt)

e=employees.select()
result = conn.execute(e)
for row in result:
    print(row)