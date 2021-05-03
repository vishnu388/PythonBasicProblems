"""
@date = '20/04/2021'
@modified_date = '21/04/2021'
@author = 'vishnu'
@Title = 'Harmonic Number '
"""
import logging

from Basiclogger import logger

logger.setLevel(logging.INFO)
try:
    n=int(input('Enter the value of N:'))
    """
    Description:
    :The input format is in integer
    Parameters:
    :integer value is must be greaterthan zero."""
    if n<=0:
        logger.info('Please enter value greater then 0')
    else:
        Result=0
        for i in range(1, n+1):
            #The Range between 1 to n+1
            # Every time of the loop taking the sum of the next harmonic number
            H=1/i
            Result+=H
            print(n, "th Value", 1 / i)
            logger.info(Result)
except Exception as e:
    logger.info(e)