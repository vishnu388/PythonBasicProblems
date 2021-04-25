"""
date = '20/04/2021'
modified_date = '21/04/2021'
author = 'vishnu'
description = 'Harmonic Number '
"""

n=int(input('Enter the value of N:'))
if n<=0:
    print('Please enter value greater then 0')
else:
    Result=0
    for i in range(1, n+1):
        # Every time of the loop taking the sum of the next harmonic number
        H=1/i
        Result+=H
        print(n, "th Value", 1 / i)

print(Result)