# function returns another function
def hello():
    def hi():
        print("hello Python")
    return hi 

new = hello()
new()