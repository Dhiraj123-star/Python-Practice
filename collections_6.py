import collections

#initialise the dictionaries 

d1 ={"Python":1,"Java":2,"C++":3}
d2={"First":1,"Second":2,"Third":3}
d3={"HTML":5}

# initialsing the chainmap
chain=collections.ChainMap(d1,d2)

# printing chainMap

print(chain)

# using new_child() to add new dictionary 

chain1= chain.new_child(d3)

print("Displaying new ChainMap")
print(chain1)