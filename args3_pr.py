# use of **kwargs in python

def whatTechTheyUsed(**kwargs):
    result=[]
    for key,value in kwargs.items():
        result.append("{} uses {}".format(key,value))
    return result

print(whatTechTheyUsed(Google="Angular",FackBook='react',
    Microsoft=".NET"))