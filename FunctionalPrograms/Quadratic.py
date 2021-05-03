"""
@date = '23/04/2021'
@modified_date = '23/04/2021'
@author = 'vishnu'
@Title = 'Write a program Quadratic.py to find the roots of the equation a*x*x + b*x + c. Since the equation is x*x, hence there are 2 roots.'
"""
import cmath
def QuadraticCalculation(a, b, c):
    """
    description:
    :in that define function as QuadraticCalculation
    parameters:
    :in that assign three variables like a, b and c
    :Here writing formula for (b.b-4ac)
    :we are import cMath function."""
    import logging
    from Functionslog import logger
    logger.setLevel(logging.INFO)
    try:
        # Calculation
        delta= (b*b)-(4*a*c)
        root1=(-b + cmath.sqrt(delta))/(2*a)
        root2=(-b - cmath.sqrt(delta))/(2*a)

        # printing value
        logger.info(root1)
        logger.info(root2)
    except Exception as e:
        logger.info(e)

try:
    # input values
    a=int(input('enter value of a: '))
    b=int(input('enter value of b: '))
    c=int(input('enter value of c: '))
    QuadraticCalculation(a, b, c)
except Exception as e:
    logger.info(e)