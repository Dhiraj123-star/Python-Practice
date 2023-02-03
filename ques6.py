# global variable in python
global_var =0
def modify_global_var():
    global global_var # setting global_var as global variable 
    global_var =100

def printing_global_var():
    print(global_var) # there is no need to declare global variable
modify_global_var()
printing_global_var() # prints 100