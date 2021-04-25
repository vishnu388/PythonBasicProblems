"""
date = '23/04/2021'
modified_date = '23/04/2021'
author = 'vishnu'
description = 'Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke
                (i.e. has no money) or reach $goal. Keeps track of the number of times he/she wins and the
                 number of bets he/she makes. Run the experiment N times, averages the results, and prints them out.'
"""
import random
#initially Stake and goal
stake = 100
goal = 200
#initially win=0 and loose=0
win = 0
loose = 0
#while loop till gambler stake=0 or stake =goal(200)
while (stake > 0 and stake < goal):
    # random var for win or loose
    gamble = random.randint(0, 1)
    if gamble == 0:
        # if gambler looses stake-1 and number of loose-1
        stake -= 1
        loose += 1
    else:
        # if wins stake++ and win++
        stake += 1
        win += 1
#printing number of wins
print("number of wins: ", +win)
winPercentage = (win * 100) / (win + loose)
losspercentage = 100 - winPercentage
#printing win percentage
print("win percentage is: ", +winPercentage)
print("Loss percentage is: ", +losspercentage)