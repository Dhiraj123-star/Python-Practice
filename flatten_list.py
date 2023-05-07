def flatten_list(nested_list):
    flattened=[]
    for item in nested_list:
         if isinstance(item,list):
              flattened.extend(flatten_list(item))
         else :
            flattened.append(item)

    return flattened

nested_list = [1,[23,45],[4,[67,78]]]

flatten_list= flatten_list(nested_list) # type: ignore

print(flatten_list)


