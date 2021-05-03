"""
@date = '20/04/2021'
@modified_date = '21/04/2021'
@author = 'vishnu'
@Title = 'Power of 2 '
"""
import math
import logging
from Basiclogger import logger
logger.setLevel(logging.INFO)
"""
Description:
:we are define function as power
Parameters:
:in that function we are assign the input like integer format."""
try:

	N = int(input('enter number from 1 to 31: '))
	if N > 31 and N >= 0:
		print('please enter number from 1 to 31')
	else:
		for i in range(N):
			result = pow(2, i)
			logger.info(result)
except Exception as e:
	logger.info(e)
