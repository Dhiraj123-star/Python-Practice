# remove the duplicates from the list 

def remove_duplicates(nums):
    uniques_items=[]
    for num in nums:
        if num not in uniques_items:
            uniques_items.append(num)
    return uniques_items

# call the function

nums =[12,44,66,12,44,80]

print("the unique nums are: ",remove_duplicates(nums))

