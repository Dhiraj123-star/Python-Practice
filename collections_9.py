# deque is the optimised list for quicker append and pop 
# operations from both sides of the container

from collections import deque

# declaring deque 

queue = deque(['name','age','DOB'])

print(queue)

queue1 = deque([1,3,8])

queue1.append(12)
print("After appending ",end="")
print(queue1)

# the appendleft() to append at the beginning 
queue1.appendleft(100)

print("After appending at the left ")
print(queue1)

# pop () method 

queue1.pop()

print("After deletion with pop() ")
print(queue1)

# popleft() method

queue1.popleft()
print("After deletion with popleft() ")
print(queue1)
