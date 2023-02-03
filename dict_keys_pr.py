# increment values of the key 
d1={"k1":10,"k2":20,"k3":30}

for i in d1.keys():
    d1[i]=d1[i]+1

print("After increment by 1",d1.values())

