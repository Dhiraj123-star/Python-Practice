import requests

req= requests.get("http://www.edureka.co/")

print(req.encoding) # returns UTF-8
print(req.status_code) #200
print(  req.elapsed) # 0:00:00.465494
print(req.url) #https://www.edureka.co:443/
print(req.history)
print(req.headers["Content-Type"]) # text/html ; charset = UTF-8
