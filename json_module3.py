# format the output
import json

with open("horoscope_data.json","r") as f:
    data = json.load(f)


# format the output 

formatted_data = json.dumps(data,indent=2)
print(formatted_data)

# command line tool for json formatting

# python -m json.tool horoscope_data.json(file name)

'''
You can also redirect the formatted output to an output file 
by specifying the output file name as the second argument:

python -m json.tool horoscope_data.json formatted_data.json

This command formats the JSON data from horoscope_data.json and
 saves the formatted output to formatted_data.json.


'''