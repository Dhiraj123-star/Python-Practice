# program for demonstrate the orderedDict

from collections import defaultdict

# defining the Dict
d=defaultdict(list)

for i in range(10):
    d[i].append(i)

print(d)