# Rest and python :Consuming APIs
# using get method
# get allows you to retrieve resources from a given APIs
# requests library is used for managing APIs
import requests
api_url="https://jsonplaceholder.typicode.com/todos/1"

response= requests.get(api_url)
print(response.json())
print("Status: ",response.status_code)# 200 (successful)
print("Response header: ",response.headers["Content-Type"])