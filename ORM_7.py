from sqlalchemy import column, create_engine,MetaData,Table,Column,Integer,String,ForeignKey

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
meta.create_all(engine)

print("Tables created successfully!!")