# the decode() function is used to convert the JSON
# object into python-format type
import demjson

var = '{"a":1,"b":2,"c":3,"d":4}'

txt= demjson.decode(var)
print(txt)