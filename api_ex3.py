# another method to create resource
import requests
import json

api_url="https://jsonplaceholder.typicode.com/todos/"

todo={
    "userId":2,
    "title":"Programming",
    "Completed":False
}

headers = {"Content-Type":"application/json"}
response= requests.post(api_url,data=json.dumps(todo),headers=headers)

print(response.json())

print("Status: ",response.status_code)