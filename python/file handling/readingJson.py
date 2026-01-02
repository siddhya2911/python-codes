import json
with open("data.json",'r')as file:
    reader=json.load(file)
print(reader)
print(reader['name'])
print(reader['age'])
print(reader['skill'])