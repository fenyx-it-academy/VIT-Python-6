#  1. Rastgele Sayi Tahmini
# 1'den 100'e kadar rastgele bir tam sayı seçen bir program yazınız. 
# Programınız kullanıcıdan tahminler istemelidir – 
# eğer kullanıcı yanlış tahmin ederse, tahminin çok yüksek veya çok düşük olduğunu yazdırmalıdır.
# Kullanıcı doğru tahmin ederse, program kullanıcının doğru cevabı tahmin etmek için ne kadar zaman harcadığını yazdırmalıdır. 
# Kullanıcının geçerli girdi girip girmedigini kontrol etmeniz de gerekmektedir.


import random

number = random.randint(1, 100)
guess = None
count = 0

while guess != number:
    try:
        guess = int(input("1 ile 100 arasında bir tam sayı girin: "))
    except ValueError:
        print("Geçersiz bir giriş yaptınız. Lütfen bir tam sayı girin.")
        continue
        
    count += 1
    
    if guess < number:
        print("Çok düşük bir sayı girdiniz. Tekrar deneyin.")
    elif guess > number:
        print("Çok yüksek bir sayı girdiniz. Tekrar deneyin.")
    else:
        print(f"Tebrikler! {count} tahminde doğru sayıyı buldunuz!")










# =================================
# 2. Zar Yüzdesi
# Zar adlı 6 öğeli bir liste oluşturun. Bu listeyi sıfır değeriyle doldurun. 5000 kez tekrarlayarak 1 ile 6 arasında (tıpkı bir zar gibi) rastgele bir sayı oluşturun.

# Değer 1 ise, listedeki 0 öğesini 1 artırın, aynısı 2, 3, 4, 5 ve 6 değerleri için de geçerlidir. dice[0] öğesi, 1 değerinin kaç kez oluştuğunu gösterir. Veya genel olarak: zar[x-1], x'in kaç kez atıldığını gösterir.

# Tekrarın sonunda, listenin içeriğini 2 ondalık basamakla yüzde olarak yazdırın. Örneğin; "3 değerindeki atışların yüzdesi = %16,28"

import random

dice = [0] * 6

for i in range(5000):
    roll = random.randint(1, 6)
    dice[roll-1] += 1

for i in range(6):
    percentage = dice[i] / 50
    print(f"{i+1} değerindeki atışların yüzdesi = %{percentage:.2f}")







# =================================
# 3. Basic Import
# my_dice.py adlı bir Python modülü oluşturun ve 
# 2. soruda yazdığınız kodu rollDice(sayı) adlı bir fonksiyona aktarın.

import my_dice

num = int(input("Tekrar numarasını girin: "))

percentages = my_dice.rollDice(num)

for i in range(6):
    print(f"{i+1} olasılığı %{percentages[i]:.2f}")
    
    
