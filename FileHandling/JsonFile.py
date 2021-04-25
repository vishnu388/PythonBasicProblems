import json
dictionary={
    "name": "Vardhan",
    "State": "AndhraPradesh",
    "code": 27,
    "phonenumber": "8106261925",
    "email": "a.vishnu388@gmail.com"
}
json_obj = json.dumps(dictionary, indent=5)

with open("sample.json", "w") as outfile:
       outfile.write(json_obj)