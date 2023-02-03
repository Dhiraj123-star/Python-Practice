
# Write a Program to combine two different dictionaries. 
# While combining, if you find the same keys, 
# you can add the values of these same keys.
#  Output the new dictionary

from collections  import Counter 

d1 = {'key1':30,'key2':100,'key3':200,'key4':10}
d2 = {'key1':40,'key2':100,'key3':90}

new_dict = Counter(d1)+Counter(d2)

print(new_dict) 