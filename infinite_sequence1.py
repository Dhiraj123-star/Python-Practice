# infinite sequence in python

def infinite():
    n=0
    while True:
        yield n
        n+=1

for i in infinite():
    if i%4==0:
        continue
    elif i==13:
        break
    else:
        print(i)

