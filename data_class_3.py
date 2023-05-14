from dataclasses import dataclass

@dataclass
class Programming_lang :
    name:str
    rank:int
    features:str

# create object 

pr = Programming_lang("Python",1,"Easy to learn, General-purpose, Best Programming language")

print(pr)