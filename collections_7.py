# NamedTuple
# returns a Tuple object with names for each position
# which the ordinary tuples lack.

from collections import namedtuple

# declaring namedTuple()

Student= namedtuple('Student',['name','age','address'])
# adding values 
S= Student('Nandini',34,'Gurgaon')

# accessing using index

print("The Student age using index:",end=" ")
print(S[1])

# access using name 

print("The Student name using keyname is:",end=" ")
print(S.name)