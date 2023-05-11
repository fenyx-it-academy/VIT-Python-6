def roolDice(sayi):
    import random
    dice = [0,0,0,0,0,0]

    for i in range(sayi):
        dice[random.randint(0,5)] += 1

    # print (dice)

    for i in range(0,6):
        dice[i] = ((dice[i]/sayi)*100)
        print(f" {i+1} değerindeki atışların yüzdesi = % {dice[i]:.2f}")
