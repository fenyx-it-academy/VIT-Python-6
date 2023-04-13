
import random

def rollDice(num):
    dice = [0, 0, 0, 0, 0, 0]

    for i in range(num):
        roll = random.randint(1, 6)
        dice[roll-1] += 1

    percentages = []
    for i in range(6):
        percentage = (dice[i] / num) * 100
        percentages.append(percentage)
    
    return percentages
