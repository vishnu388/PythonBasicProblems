import json
#Reading json file
with open('person.json') as f:
  data = json.load(f)
# Output: {'name': 'Venkat', 'languages': ['English', 'Telugu']}
print(data)


#Convert dict to json
person_dict = {'name': 'Kiran',
'age': 25,
'Education': 'PharmD'
}
person_json = json.dumps(person_dict)
# Output: {"name": "Kiran", "age": 25, "Education": PharmD}
print(person_json)


#write to json file
person_dict = {"name": "vishnu",
"languages": ["English", "Telugu"],
"married": False,
"age": 23
}

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)

#printing json object
print(json.dumps(person_dict, indent = 4, sort_keys=True))