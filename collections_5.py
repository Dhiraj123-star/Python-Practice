# chainmap 
# encapsulates many dictionaries into one 

from collections import ChainMap
d1={'a':1,'b':2,'c':3}
d2={'d':4,'e':5,'f':6}
d3={'g':7,'h':8}

# defining the chainmap
c=ChainMap(d1,d2,d3)

print(c)

# accessing the value using keyname
print(c['c'])

# accessing values using values method
print(c.values())

# accessing keys using keys method
print(c.keys())