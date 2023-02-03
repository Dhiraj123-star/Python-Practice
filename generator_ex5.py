# infinite iterator using python generator
def myinfinite():
    num= 0
    while True:
        yield num
        num+=1
for i in myinfinite():
    print(i) # it will print infinite number 
    