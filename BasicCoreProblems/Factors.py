"""
@date = '20/04/2021'
@modified_date = '21/04/2021'
@author = 'vishnu'
@Title = 'Prime Facterization '
"""

import math
import logging
from Basiclogger import logger
logger.setLevel(logging.INFO)
try:
    class Factors:
        def Factors(self):
            """
            Description:
            Here we are defining the functions as factor
            Parameters:
            :the input as integer format"""
            print("Enter Number : ")
            n = int(input())
            print("Prime factors for", n, "is")
            #Printing the factors of a given number until it is divided by 2.
            while n % 2 == 0:
                    logger.info("2")
                    n = n / 2
            #If the given number is not even then this loop will print the remaining factors.
            for i in range(3, int(math.sqrt(n)+1)):
                while n % i == 0:
                    logger.info(i);
                    n = n / i
                i+=2
            #If the remaining factor is greater than 2 it will be printing
            if n > 2:
                logger.info(n)
            else:
                print()
    nums = Factors()
    nums.Factors()
except Exception as e:
    logger.info(e)