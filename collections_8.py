# namedTuple

from collections import namedtuple

# declaring namedTuple

Student = namedtuple('Student',['name','age','DOB'])

# adding values 

S= Student('Rahul',19,'2451999')

# initialising iterable 

li=['Manjeet',25,'452000']

#initialising dict 
di={'name':'Nikhil','age':34,'DOB':'1291997'}

# using _make() to return namedTuple

print(Student._make(li))

# using _asdict() to return an OrderedDict()

print(S._asdict())
