"""
@date = '20/04/2021'
@modified_date = '21/04/2021'
@author = 'vishnu'
@Title = 'User Input and Replace String Template “Hello <<UserName>>, How are you?”'
"""
import logging

from Basiclogger import logger

logger.setLevel(logging.INFO)
try:
    """
    Description:
    :we are replace the string Template "Hello <<UserName>>, How are you?"
    parameters:
    :in we are assign input String format"""

    String = "Hello <<UserName>>, How are you?"
    """we pass the input as String format"""
    name= str(input("Enter your name: "))
    if len(name) < 3:
        logger.info('min name length is 3 characters')
    else:
        string = String.replace("<<UserName>>",name)
        logger.info(string)
except Exception as e:
        logger.info(e)
