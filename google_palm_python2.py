import google.generativeai as palm 

palm.configure(api_key="AIzaSyCOMwJ37ZsuowV-Bfnm7k6EQ2IvrF1Vko67") # replace with your API-key

response = palm.generate_text(prompt='Tell me about prompt engineering using Python')

print(response.result)