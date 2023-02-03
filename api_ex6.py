# Delete () method to delete completely the resource
import requests

api_url="https://jsonplaceholder.typicode.com/todos/10"

response= requests.delete(api_url)
print(response.json())
print("Status: ",response.status_code)