# meta class in Python 

''' Python Metaclass sets the behavior and rules of a class'''

class MetaClassEx(type):
    def __init__(cls,name,base,dict):
        cls.attribute ='Python meta class concept'

class MetaTest(metaclass=MetaClassEx):
    pass 

print(MetaTest.attribute)