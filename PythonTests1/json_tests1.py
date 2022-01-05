import json

with open("json_sample1.json") as data:
    json_data = data.read()

#print(json_data)

json_dict = json.loads(json_data)

print(json_dict)
