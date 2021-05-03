# Python program to read JSON
# from a file


import json
try:
    class Readjson:
        def readjson(self):
            # Opening JSON file
            with open('sample.json', 'r') as openfile:
                # Reading from json file
                json_object = json.load(openfile)

            print(json_object)
            print(type(json_object))
    # creating object for the class and calling the method
    Json = Readjson()
    Json.readjson()
except Exception as e:
    print(e)
