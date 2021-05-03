"""
@date = '20/04/2021'
@modified_date = '21/04/2021'
@author = 'vishnu'
@Title = 'Flip Coin and print percentage of Heads and Tails'
"""

import random
import logging
from Basiclogger import logger

try:
    logger.setLevel(logging.INFO)
    class FlipCoin:
        def printing(self):
            """
            Description:
            taking input from the user no of times to flip the coin
            Parameters:
            :the input in integer format
            :The initial position is zero for both"""
            print("Enter no of time to flip coin :")
            n = int(input())
            head=0
            tail=0
            if n!=0:
                for i in range(0, n):
                    #Taking random number for each time of the loop running.
                    x = random.random()
                    #If random number is less than 0.5 it counted as Tails else false.
                    if x<0.5:
                        head=head+1
                    else:
                        tail=tail+1
                #Finding the percentage of heads and tails.
                headPercentage = head*100/n
                tailPercentage = tail*100/n
                logger.info(headPercentage)
                logger.info(tailPercentage)
                print("Head Percentage = ", headPercentage, "%")
                print("Tail Percentage = ", tailPercentage, "%")
            else:
                #You give input in null value its shows no result.
                print("You have entered 0 Value, it is not possible")
    # creating object for the class and calling the method
    flipcoin = FlipCoin()
    flipcoin.printing()
except Exception as e:
    logger.exception(e)