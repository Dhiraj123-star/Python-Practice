# generator in Python that returns the traversal object
# used to create iterators.

def simple():
    for i in range(1,11):
        if(i%2!=0):
            yield i

# successive function call using for loop
for i in simple():
    print(i)

