# reading the json file 

import json

# retrieve JSON data from the file

with open("horoscope_data.json","r") as f:
    data =json.load(f)

# access and process the retrieved JSON data 

date =data['data']['date']

horoscope_data = data['data']['horoscope_data']

print(f"Horoscope for date {date}: {horoscope_data}")



