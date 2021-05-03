"""
@date = '27/04/2021'
@modified_date = '27/04/2021'
@author = 'vishnu'
@Title = ' Write a Program to play a Cross Game or Tic-Tac-Toe Game.'
"""
import random
import logging

from Logicallog import logger

logger.setLevel(logging.INFO)
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

#displaying board
def printBoard(board):
    logger.info(board['1'] + '  |  ' + board['2'] + '  |  ' + board['3'])
    logger.info('-  +  -  +  -')
    logger.info(board['4'] + '  |  ' + board['5'] + '  |  ' + board['6'])
    logger.info('-  +  -  +  -')
    logger.info(board['7'] + '  |  ' + board['8'] + '  |  ' + board['9'])


def main_game():
    turn = 'X'
    count = 0

    for i in range(1,10):
        printBoard(theBoard)
        logger.info("It's your turn," + turn + "Enter the number between 1 to 9 :")
        move = input()
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            logger.info("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                logger.info("\nGame Over.\n")
                logger.info(" **** " + turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                logger.info("\nGame Over.\n")
                logger.info(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                logger.info("\nGame Over.\n")
                logger.info(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                logger.info("\nGame Over.\n")
                logger.info(" **** " + turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                logger.info("\nGame Over.\n")
                logger.info(" **** " + turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                logger.info("\nGame Over.\n")
                logger.info(" **** " + turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                logger.info("\nGame Over.\n")
                logger.info(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                logger.info("\nGame Over.\n")
                logger.info(" **** " + turn + " won. ****")
                break

        if count == 9:
            logger.info("\nGame Over.\n")
            logger.info("Draw!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

if __name__ == "__main__":
    main_game()