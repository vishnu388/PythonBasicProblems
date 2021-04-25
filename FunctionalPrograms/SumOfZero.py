"""
date = '21/04/2021'
modified_date = '22/04/2021'
author = 'Vishnu'
description = 'A program with cubic running time. Read in N integers and counts the   number of triples that sum to exactly 0.'
"""

def findTriplets(array, n):
    try:
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if array[i] + array[j] + array[k] == 0:
                        found = True
                        print(array[i], array[j], array[k])

    except Exception as e:
        print(e)

        # If no triplet with 0 sum
    # found in array
    if found == False:
        print(" not exist ")


# main function
array = [0, -1, 2, -3, 1]
n = len(array)
findTriplets(array, n)