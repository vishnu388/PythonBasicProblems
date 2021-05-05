import os
from decouple import config
print(config("user"))
print(config("passwd"))
print(config("host"))
#print(os.environ.get("user"))