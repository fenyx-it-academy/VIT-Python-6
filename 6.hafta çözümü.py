#Rastgele Sayi Tahmini
import time
import random
cpu = int(random.randint(0,100))

baslangic = time.time()
while True:
    try:
        tahmin = int(input("0 - 100 arasi sayiyi tahmin et:"))
        if tahmin < 0:
            raise ArithmeticError("Pozitif bir tam sayi girin!")

    except ValueError:
        print("0-100 arasi bir sayi girin!")
        continue
    
    if tahmin == cpu:
        print("Dogru bildin!")
        break
    elif tahmin > cpu:
        print("Yuksek tahmin")
    elif tahmin < cpu:
        print("Dusuk tahmin")

bitis = time.time()
print("Tahmin Suresi:",bitis - baslangic)

#Zar yuzdesi
import random

zar =[[0],[0],[0],[0],[0],[0]]

tekrar = 5000

while tekrar > 0:
    gelen_sayi = random.randint(1,6)
    tekrar -= 1
    if gelen_sayi == 1:
        zar[gelen_sayi-1][0] += 1
    elif gelen_sayi == 2:
        zar[gelen_sayi-1][0] += 1 
    elif gelen_sayi == 3:
        zar[gelen_sayi-1][0] += 1 
    elif gelen_sayi == 4:
        zar[gelen_sayi-1][0] += 1 
    elif gelen_sayi == 5:
        zar[gelen_sayi-1][0] += 1 
    elif gelen_sayi == 6:
        zar[gelen_sayi-1][0] += 1 


for x,y in enumerate(zar,1):
    print("{} degerinin gelme olasiligi:{}".format(x,y[0] /100))
    
#Basic Import
from random import randint

def rollDice(sayi):
    zar =[["bir",0],["iki",0],["uc",0],["dort",0],["bes",0],["alti",0]]

    sayi = 5000

    while sayi > 0:
        gelen_sayi = randint(1,6)
        sayi -= 1
        if gelen_sayi == 1:
            zar[gelen_sayi-1][1] += 1
        elif gelen_sayi == 2:
            zar[gelen_sayi-1][1] += 1 
        elif gelen_sayi == 3:
            zar[gelen_sayi-1][1] += 1 
        elif gelen_sayi == 4:
            zar[gelen_sayi-1][1] += 1 
        elif gelen_sayi == 5:
            zar[gelen_sayi-1][1] += 1 
        elif gelen_sayi == 6:
            zar[gelen_sayi-1][1] += 1 

    print("Zar'in 1 gelme olasiligi:",float(zar[0][1]/100))
    print("Zar'in 2 gelme olasiligi:",float(zar[1][1]/100))
    print("Zar'in 3 gelme olasiligi:",float(zar[2][1]/100))
    print("Zar'in 4 gelme olasiligi:",float(zar[3][1]/100))
    print("Zar'in 5 gelme olasiligi:",float(zar[4][1]/100))
    print("Zar'in 6 gelme olasiligi:",float(zar[5][1]/100))
    
    
#MY_main
import my_dice

try:
    tekrar = int(input("Tekrar sayisini girin:"))
except ValueError:
    print("Pozitif bir sayi girin!")
except:
    print("Hata Olustu!")

my_dice.rollDice(tekrar)
