import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")

file = open("name-mapping.csv")
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()

for user in rows:
    source = os.path.join(IMAGE_DIR, str(user[0]))
    destination = os.path.join(IMAGE_DIR, str(user[1]))
    print(source,destination)
    try:
        os.rename(source, destination)
    except:
        print("No directory")

