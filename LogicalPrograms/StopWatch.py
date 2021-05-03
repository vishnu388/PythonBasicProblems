"""
@date = '24/04/2021'
@modified_date = '24/04/2021'
@author = 'vishnu'
@Title = 'Write a Stopwatch Program for measuring the time that elapses between the start and end clicks'
"""

import time
import logging

from Logicallog import logger

logger.setLevel(logging.INFO)
try:
    def time_convert(sec):
        """
        Description:
        :we are define function as time_convert
        parameters:
        :in hours converted into mins
        :in mins converted into sec
        """
        mins = sec // 60
        #sec = sec % 60
        hours = mins // 60
        #mins = mins % 60

        logger.info("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))

    input("Press A to start :")
    start_time = time.time()
    input("Press S to stop :")
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(round(time_lapsed))
except Exception as e:
    logger.info(e)