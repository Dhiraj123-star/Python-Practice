# data class in Python

from dataclasses import dataclass

@dataclass
class Person:
    name:str
    age:int 


person = Person("Prakash",16)

print(person.name)
print(person.age)