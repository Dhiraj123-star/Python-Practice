# patch () method to modify the value of a specific field
# on the existing todo. Patch differs from PUT in that it
# doesn't completely replace the existing resource.

import requests
api_url="https://jsonplaceholder.typicode.com/todos/10" 
todo={
    "title":"Python APIs Programming"
}
response = requests.patch(api_url,json=todo)

print(response.json())
print("Status: ",response.status_code)