"""
@date = '23/04/2021'
@modified_date = '23/04/2021'
@author = 'vishnu'
@Title = 'Write a program Distance.py that takes two integer command-line arguments x and y and
                prints the Euclidean distance from the point (x, y) to the origin (0, 0). The formulae to
                calculate distance = sqrt(x*x + y*y). Use Math.power function'
"""

import math
import logging
from Functionslog import logger
logger.setLevel(logging.INFO)
def CalculateDistance(x, y):
    """
    description:
    :In that define function as  CalculateDistance
    parameters:
    :we are assign two variables x and y
    :we define Math function."""
    # calculating distance
    distance= math.sqrt(pow(x, 2)+pow(y, 2))
    # print distance
    logger.info(distance)

try:
    #taking inputs x and y
    x=int(input('enter x value: '))
    y=int(input('enter y value: '))
    CalculateDistance(x, y)
except Exception as e:
    logger.info(e)