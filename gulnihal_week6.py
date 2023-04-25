#soru1
import random
import time
bilgisayar=random.choice(range(1,100))
baslangic=time.time()
while True:
    try:
        secim=int(input("1 ile 100 arasinda sececegim sayiyi tahmin et:"))
        if secim==bilgisayar:
            print("Evet dogru bildin!!")
            bitis= time.time()
            gecen_sure = bitis- baslangic
            print(f"{round(gecen_sure)} saniyede tuttugum sayiyi bildiniz.")
            break
        elif secim<bilgisayar:
            print("Biraz daha yuksek bir sayi secmelisin!")
        elif secim>bilgisayar:
            print("Biraz daha kucuk bir sayi secmelisin!") 
        else:
         continue    
    except ValueError:("Lutfen 0'dan buyuk bir tam sayi giriniz.")
      
      
#soru2
import random

dice = [0, 0, 0, 0, 0, 0]  # 6 öğeli bir liste oluşturun ve sıfır değeriyle doldurun

for i in range(5000):  # 5000 kez tekrarlayın
    roll = random.randint(1, 6)  # 1 ile 6 arasında bir rastgele sayı oluşturun
    dice[roll-1] += 1  # ilgili öğeyi 1 artırın

      # Sonuçları yüzdelik olarak yazdırın
for i in range(6):
    percent = (dice[i] / 5000) * 100
    print(f"{i+1} degerindeki atislarinn yuzdesi = {percent:.2f}%")
    
    
#soru3
import random

def rollDice(numRolls):
    dice = [0, 0, 0, 0, 0, 0]  # 6 öğeli bir liste oluşturun ve sıfır değeriyle doldurun

    for i in range(numRolls):  # numRolls kez tekrarlayın
        roll = random.randint(1, 6)  # 1 ile 6 arasında bir rastgele sayı oluşturun
        dice[roll-1] += 1  # ilgili öğeyi 1 artırın

    # Sonuçları yüzdelik olarak hesaplayın ve döndürün
    percentages = [(x / numRolls) * 100 for x in dice]
    return percentages

from soru3 import rollDice

numRolls = int(input("Tekrar numarasını girin: "))
percentages = rollDice(numRolls)

     # Her olasılığı yazdırın
for i in range(6):
    print(f"{i+1} olasılığı {percentages[i]:.2f}'dir")


