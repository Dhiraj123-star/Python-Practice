# set comprehension using Python

blue_set = {"blue","blue","blue","blue"} # it stores only unique set of items 
print(blue_set) 

red_set = {"red" for _ in blue_set}

print(red_set) # it stores only unique set of items 

