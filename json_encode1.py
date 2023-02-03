# Encoding is defined as converting the text or values into an encrypted form
# that can only be used by the desired user through decoding it.
import demjson

var =[{ 
    "Math":50, "Physics":90,"Chemistry":100
    }]

print(demjson.encode(var))