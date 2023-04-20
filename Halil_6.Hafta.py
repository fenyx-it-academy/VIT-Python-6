# CEVAP_1_________________________

import random
import time
start = time.perf_counter()
pc = random.randint(1, 100)
while True:

    try:
        user = int(input("Tahmininiz? :"))

        if pc > user and pc - user >= 10:
            print("Tahmininiz cok dusuk\n\n")
            continue

        elif pc > user and pc - user < 10:
            print("Yaklastiniz ama yinede tahmininiz dusuk\n\n")
            continue

        elif pc < user and user - pc >= 10:
            print("Tahmininiz cok yuksek\n\n")
            continue

        elif pc < user and user - pc < 10:
            print("Yaklastiniz ama yinede tahmininiz yuksek\n\n")
            continue

        else:
            print("BINGO!! Bildiniz")
        break

    except:
        print("Tam sayi girmediniz\n\n")
finish = time.perf_counter()
print("Skor : ", round(finish - start), "saniye!!")

# CEVAP_2_________________________

import random

zar = [0, 0, 0, 0, 0, 0]
count = 0
while count < 5000:
    tekrar = random.randint(1, 6)
    if tekrar == 1:
        zar[0] += 1
    elif tekrar == 2:
        zar[1] += 1
    elif tekrar == 3:
        zar[2] += 1
    elif tekrar == 4:
        zar[3] += 1
    elif tekrar == 5:
        zar[4] += 1
    elif tekrar == 6:
        zar[5] += 1
    count += 1

print(f"""
1 degerindeki atislarin yuzdesi = %{round((zar[0]/50),2)}
2 degerindeki atislarin yuzdesi = %{round((zar[1]/50),2)}
3 degerindeki atislarin yuzdesi = %{round((zar[2]/50),2)}
4 degerindeki atislarin yuzdesi = %{round((zar[3]/50),2)}
5 degerindeki atislarin yuzdesi = %{round((zar[4]/50),2)}
6 degerindeki atislarin yuzdesi = %{round((zar[5]/50),2)}
""")

# CEVAP_3_________________________
my_dice.py

import random


def roll_dice(sayi):
    zar = [0, 0, 0, 0, 0, 0]
    count = 0
    while count < sayi:
        tekrar = random.randint(1, 6)
        if tekrar == 1:
            zar[0] += 1
        elif tekrar == 2:
            zar[1] += 1
        elif tekrar == 3:
            zar[2] += 1
        elif tekrar == 4:
            zar[3] += 1
        elif tekrar == 5:
            zar[4] += 1
        elif tekrar == 6:
            zar[5] += 1
        count += 1

    list = []
    for i in zar:
        a = (round((i * 100 / sayi), 2))
        list.append(a)

    return (f"""
    1 degerindeki atislarin yuzdesi = %{list[0]}
    2 degerindeki atislarin yuzdesi = %{list[1]}
    3 degerindeki atislarin yuzdesi = %{list[2]}
    4 degerindeki atislarin yuzdesi = %{list[3]}
    5 degerindeki atislarin yuzdesi = %{list[4]}
    6 degerindeki atislarin yuzdesi = %{list[5]}
        """)





##########################################
main.py


from my_dice import roll_dice
while True:
    try:
        user = int(input("Tekrar numarasını girin: "))
        print(roll_dice(user))
        if user <= 0:
            raise Exception("Lutfen 0 dan yuksek bir sayi giriniz")
            continue
    except ValueError:
        print("Lutfen tam sayi giriniz")
