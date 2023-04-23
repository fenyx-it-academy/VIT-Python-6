cevap1
#1'den 100'e kadar rastgele bir tam sayı seçen bir program yazınız.
# Programınız kullanıcıdan tahminler istemelidir –
# eğer kullanıcı yanlış tahmin ederse, tahminin çok yüksek veya çok düşük olduğunu yazdırmalıdır.
# Kullanıcı doğru tahmin ederse, program kullanıcının doğru cevabı tahmin etmek için ne kadar zaman harcadığını yazdırmalıdır. 
#Kullanıcının geçerli girdi girip girmedigini kontrol etmeniz de gerekmektedir.

import random
import time
print('1 ile 100 arasinda tutulan sayinin tahmini ')
start_time=time.time()
bilg_secim=random.randint(1,100)
sayac=0
while True:
           
      kullanici_secim=input("Tahmininizi giriniz:")
      sayac+=1
      if not kullanici_secim.isdigit() or int(kullanici_secim)<1 or int(kullanici_secim)>100:
            print('Hata!! 1 ile 100 arasinda sayi degeri giriniz')
            continue
      kullanici_secim=int(kullanici_secim)
      if bilg_secim<kullanici_secim:
            print('Yuksek Tahmin')
      elif bilg_secim>kullanici_secim:
            print('Dusuk Tahmin')
      else:
            print('Dogru Tahmin')
            end_time=time.time()
            break

tahmin_sure=end_time-start_time
print(f'Tahmin suresiniz {tahmin_sure:.2f} sn.dir.{sayac} seferde bildiniz')

cevap2
#Zar adlı 6 öğeli bir liste oluşturun. Bu listeyi sıfır değeriyle doldurun. 
# 5000 kez tekrarlayarak 1 ile 6 arasında (tıpkı bir zar gibi) rastgele bir sayı oluşturun.
# Değer 1 ise, listedeki 0 öğesini 1 artırın, aynısı 2, 3, 4, 5 ve 6 değerleri için de geçerlidir. dice[0] öğesi,
# 1 değerinin kaç kez oluştuğunu gösterir. Veya genel olarak: zar[x-1], x'in kaç kez atıldığını gösterir.
# Tekrarın sonunda, listenin içeriğini 2 ondalık basamakla yüzde olarak yazdırın. Örneğin; "3 değerindeki atışların yüzdesi = %16,28"
import random

zar = [0, 0, 0, 0, 0, 0]

for i in range(5000):
    roll = random.randint(0,5)
    zar[roll]=zar[roll]+1

for i in range(6):
    percentage = zar[i] / 5000 * 100
    print(f"{i+1} değerindeki atışların yüzdesi = %{percentage:.2f}")
    
cevap3

my_dice.py

import random

def roll_dice(sayi):
    zar = [0, 0, 0, 0, 0, 0]
    count = 0
    while count < sayi:
        roll = random.randint(0,5)
        zar[roll]=zar[roll]+1
        count += 1


    for i in range(6):
        percentage = zar[i] / sayi * 100
    return print(f"{i+1} değerindeki atışların yüzdesi = %{percentage:.2f}")
 
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
