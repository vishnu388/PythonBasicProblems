"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'vishnu'
description = 'User Input and Replace String Template “Hello <<UserName>>, How are you?”'
"""

String = "Hello <<UserName>>, How are you?"
name= input("Enter your name: ")
if len(name) < 3:
    print('min name length is 3 characters')
else:
    string = String.replace("<<UserName>>",name)
    print(string)