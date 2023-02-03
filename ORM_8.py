from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,ForeignKey

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

# insert data into students table 

conn= engine.connect()

conn.execute(students.insert(),[
    {'name':"Ravi","lastname":"Kapoor"},
    {"name":"Rajiv","lastname":"Khanna"},
    {"name":"Komal","lastname":"Bhandari"},
    {"name":"Abdul","lastname":"Sattar"},
    {"name":"Priya","lastname":"Rajhans"}
])

conn.execute(addresses.insert(),[
    {'st_id':1,"postal_add":"Shivajinagar Pune",'email_id':"ravi@gmail.com"},
    {'st_id':1,'postal_add':"ChurchGate Mumbai",'email_id':"kapoor@gmail.com"},
    {'st_id':3,'postal_add':"Jubilee Hills Hyderabad",'email_id':"komal@gmail.com"},
    {'st_id':5,'postal_add':"MG Road Bangaluru",'email_id':"as@yahoo.com"},
    {'st_id':2,'postal_add':"Cannought Place New Delhi",'email_id':"admin@khanna.com"}
])

print("Data inserted successfully into both tables")