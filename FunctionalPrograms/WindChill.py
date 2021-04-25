"""
date = '23/04/2021'
modified_date = '23/04/2021'
author = 'vishnu'
description = 'A program with cubic running time. Read in N integers and counts the   number of triples that sum to exactly 0.'
"""

def WindCalculation(Temperature, Speed):
    try:
        # calculation part
        w=35.74+(0.6215*Temperature)+((0.4275*Temperature)-35.75)*pow(Speed, 0.16)

        print('calculated windchill is: ')
        print(w)
    except Exception as e:
        print("invalid", e)

def userinput():
         Temperature= int(input('enter the value of temperature in Fahrenheit less then 50: '))
         Speed= int(input('enter wind speed in miles per hour from 3 to 120: '))
         return Temperature, Speed

Temperature, Speed = userinput()
if Speed > 120 or Speed < 3 or Temperature > 50:
    print("Can't get WindChill at this Parameters")
else:
    WindCalculation(Temperature, Speed)