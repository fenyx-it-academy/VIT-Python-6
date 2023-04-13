from my_dice import rollDice

num = int(input("Tekrar numarasini girin: "))
percentages = rollDice(num)

for i in range(6):
        print("{} olasiliği {:.2f}'dir".format(i+1, percentages[i]))