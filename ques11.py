# show the difference between list and arrays
import array as arr

# creating an array and list
array_1= arr.array('i',[12,45,56,90])
lst_1 = [4,"interview",90.6]

print(array_1)
print(lst_1)

# trying to create an array with multiple data types we got error 
# try:
#     array_2= arr.array("i",[3,7,8,"interview"])
# except Exception as e:
#     print(e)