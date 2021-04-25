"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'vishnu'
description = 'Leap Year'
"""

year=int(input('Enter year: '))
if year<999:
    print('invalid year, please enter 4 digit year value')
else:
    if year % 4 == 0 and year % 100 != 0:
        print(year, "is a Leap Year")
    elif year % 100 == 0:
        print(year, "is not a Leap Year")
    elif year % 400 ==0:
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")