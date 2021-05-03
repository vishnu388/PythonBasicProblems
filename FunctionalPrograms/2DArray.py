"""
@date = '21/04/2021'
@modified_date = '22/04/2021'
@author = 'Vishnu'
@Title = ' A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.'
"""
import logging
from Functionslog import logger
logger.setLevel(logging.INFO)
def PrintArray(Rows, Columns):

    """
    Description:
    :We are defining the function as PrintArray
    parameters:
    :in side passing two variables like Rows and Columns."""
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
            logger.info(array1[i])
            logger.info(array[j])
        logger.info()
try:
    #Here passing matrix or index(3x3)
    PrintArray(3, 3)
except Exception as e:
    logger.info(e)