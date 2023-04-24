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
1 degerindeki atislarin yuzdesi = %{(zar[0]/50):.2f}
2 degerindeki atislarin yuzdesi = %{(zar[1]/50):.2f}
3 degerindeki atislarin yuzdesi = %{(zar[2]/50):.2f}
4 degerindeki atislarin yuzdesi = %{(zar[3]/50):.2f}
5 degerindeki atislarin yuzdesi = %{(zar[4]/50):.2f}
6 degerindeki atislarin yuzdesi = %{(zar[5]/50):.2f}
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

        list.append(f"{(i * 100 / sayi):.2f}")

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

        if user <= 0:
            raise ArithmeticError("Lutfen 0 dan yuksek bir sayi giriniz")

    except ValueError:
        print("Lutfen tam sayi giriniz")
    except ArithmeticError as err:
        print(err)
    else:
        print(roll_dice(user))
