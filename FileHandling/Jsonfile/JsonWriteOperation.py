# Python program to write JSON
# to a file


import json
try:
    class Writejson:
        def writejson(self):
            # Data to be written
            dictionary = {
                "name": "Vishnu",
                "city": "ongole",
                "state": "A.P",
                "phonenumber": "8106261925"
            }


            with open("sample.json", "w") as outfile:
                json.dump(dictionary, outfile)
    # creating object for the class and calling the method
    writejson = Writejson()
    writejson.writejson()
except Exception as e:
    print(e)