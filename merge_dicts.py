# merge two dictionaries 

dict1 = {"Python":1,"Java":2,"C":3,"JavaScript":4,"Ruby":5}
dict2 = {"TypeScript":6,"Scala":7,"Julia":8,"HTML":9,"PHP":10}

merged_dict = {**dict1,**dict2}

print(merged_dict)