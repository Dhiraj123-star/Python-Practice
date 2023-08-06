# use mypy for static checking

def foo(x:int,y:int)->int:
    return x**2+y**2

foo(4,5)
# foo (90,56.7) # throw error