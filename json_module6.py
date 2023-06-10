
import json

json_str = '{"name": "Ashutosh Krishna", "age": 23, "email": "ashutosh@example.com"}'

data = json.loads(json_str)

name = data.get("name")
age = data.get("age")
email = data.get("email")

print(name)
print(age)
print(email)

