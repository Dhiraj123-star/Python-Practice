# post method to create a new resource

import requests
api_url= "https://jsonplaceholder.typicode.com/todos"
todo={
    "userId":1,
    "title":"Buy Milk",
    "Completed":False
}
response= requests.post(api_url,json=todo)

print(response.json())
print("status: ",response.status_code)# returns 201(created)
