import requests
import json

response = requests.get("https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=sagittarius&day=today")

data = response.json() # convert response data into json

# store the json data into the file


with open("horoscope_data.json","w") as f:
    json.dump(data,f)

print("json data successfully saved!!")
