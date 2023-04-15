# To find the common elements from the lists

def find_common_elements(list1,list2):
    common_element =[]
    for num in list1:
        if num in list2 and num not in common_element:
            common_element.append(num)
    return common_element

# call the function
list1 = [12,45,77,12,44,90]
list2 = [90,18,9,100,23,1000]

print("The common element is: ",find_common_elements(list1,list2))