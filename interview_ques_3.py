# WAP (Write a program) 
# which takes a sequence of numbers and check if all numbers are unique.

def check_distinct(data_list):
    if len(data_list)==len(set(data_list)):
        return True
    else:
        return False
    
# calling the function

data_list = [12,45,44,34]
print(check_distinct(data_list)) # returns True
data_list = [34,35,44,34]
print(check_distinct(data_list)) # returns False 

