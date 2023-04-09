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

if __name__ == "__main__":
    num = int(input("Tekrar numarasini girin: "))
    percentages = rollDice(num)

    for i in range(6):
        print("{} olasiliği {:.2f}'dir".format(i+1, percentages[i]))
