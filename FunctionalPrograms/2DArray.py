"""
date = '21/04/2021'
modified_date = '22/04/2021'
author = 'Vishnu'
description = ' A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.'
"""
def PrintArray(Rows, Columns):
    array1 = []
    print("Enter the entries row wise:")

    # For user input
    for i in range(Rows):  # A for loop for row entries
        array2 = []
        for j in range(Columns):  # A for loop for column entries
            array2.append(input())
        array1.append(array2)

    # For printing the array
    for i in range(Rows):
        for j in range(Columns):
            print(array1[i][j], end=" ")
        print()
try:
    PrintArray(3, 3)
except Exception as e:
    print(e)