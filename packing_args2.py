# packing with ** operator

# a dictionary items using ** 
def myfun(**kwargs):
    # print dictionary items
    for key in kwargs:
        print("%s : %s "%(key,kwargs[key]))


# driver code 
myfun(name="Dhiraj",age=24,hobby="Programming")