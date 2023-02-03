# put method is used to update the existing todo with
# new data
import requests
api_url="https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())
todo={
    "userId":1,
    'title':"Coding",
    'Completed':True
}
response= requests.put(api_url,json=todo)
print(response.json())
print("Status: ",response.status_code)