"""
@date = '20/04/2021'
@modified_date = '21/04/2021'
@author = 'vishnu'
@Title = 'Leap Year'
"""
import logging

from Basiclogger import logger

try:
    year=int(input('Enter year: '))
    logger.setLevel(logging.INFO)
    """
    Description:
    :we are defining the leap year
    Parameters:
    :We give input in integer format."""
    if year<999:
        #The input is grater than 999(year is grater than 4 digit).
        logger.info('invalid year, please enter 4 digit year value')
    else:
        if year % 4 == 0 and year % 100 != 0:
            logger.info( "is a Leap Year")
            logger.info(year)
        elif year % 100 == 0:
            logger.info(year, "is not a Leap Year")
        elif year % 400 ==0:
            logger.info(year, "is a Leap Year")
        else:
            logger.info( "is not a Leap Year")
            logger.info(year)
except Exception as e:
    logger.info(e)