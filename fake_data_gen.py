import csv
import random
from faker import Faker

fake = Faker()

data = [(fake.name(), random.randint(18, 80), fake.random_element(('Male', 'Female'))) for _ in range(100)]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Gender'])
    writer.writerows(data)

file.close()
print("file created successfully!!")