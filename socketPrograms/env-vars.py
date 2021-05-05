"""import os
from decouple import config
user = os.environ.get('root')
passwd = os.environ.get('Vishn@388')
print(user)
print(passwd)"""
import os
from decouple import config
print(config("user"))
print(config("passwd"))
print(config("host"))