# demonstrate infinite iterators 
import itertools

# for in loop 

for i in itertools.count(10,10):
    if i==100:
        break
    else:
        print(i,end=" ")