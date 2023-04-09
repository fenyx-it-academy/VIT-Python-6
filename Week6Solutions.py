#<!-- # VIT-Python-6

## 1. Rastgele Sayi Tahmini

#1'den 100'e kadar rastgele bir tam sayi seçen bir program yaziniz. Programiniz kullanicidan tahminler istemelidir – eğer kullanici yanliş tahmin ederse, tahminin çok yüksek veya çok düşük olduğunu yazdirmalidir. Kullanici doğru tahmin ederse, program kullanicinin doğru cevabi tahmin etmek için ne kadar zaman harcadiğini yazdirmalidir. Kullanicinin geçerli girdi girip girmedigini kontrol etmeniz de gerekmektedir.

import random

num = random.randint(1, 100)
guess = None
count = 0

while guess != num:
    try:
        guess = int(input("1 ile 100 arasinda bir tam sayi tahmin edin: "))
    except ValueError:
        print("Geçerli bir tam sayi girmediniz. Lütfen tekrar deneyin.")
        continue

    count += 1

    if guess > num:
        print("Çok yüksek. Tekrar deneyin.")
    elif guess < num:
        print("Çok düşük. Tekrar deneyin.")
    else:
        print("Tebrikler, doğru tahmin ettiniz!")
        print("{} defa da bildiniz.".format(count))

## 2. Zar Yüzdesi

# Zar adli 6 öğeli bir liste oluşturun. Bu listeyi sifir değeriyle doldurun. 5000 kez tekrarlayarak 1 ile 6 arasinda (tipki bir zar gibi) rastgele bir sayi oluşturun. 

# Değer 1 ise, listedeki 0 öğesini 1 artirin, aynisi 2, 3, 4, 5 ve 6 değerleri için de geçerlidir. dice[0] öğesi, 1 değerinin kaç kez oluştuğunu gösterir. Veya genel olarak: zar[x-1], x'in kaç kez atildiğini gösterir.

# Tekrarin sonunda, listenin içeriğini 2 ondalik basamakla yüzde olarak yazdirin. Örneğin; "3 değerindeki atişlarin yüzdesi = %16,28"

import random

dice = [0, 0, 0, 0, 0, 0]

for i in range(5000):
    roll = random.randint(1, 6)
    dice[roll-1] += 1

for i in range(6):
    percentage = (dice[i] / 5000) * 100
    print("{} değerindeki atişlarin yüzdesi = %{:.2f}".format(i+1, percentage))

# ## 3. Basic Import

# my_dice.py adli bir Python modülü oluşturun ve 2. soruda yazdiğiniz kodu rollDice(sayi) adli bir fonksiyona aktarin.
# Fonksiyon, 5000 defa tekrar yerine, verilen sayi değişkeni kadar tekrar yapar.
# Listeyi yazdirmak yerine, yüzde listesini döndürür.
# Ardindan main.py adli yeni bir modül oluşturun. 
# "Tekrar numarasini girin:" yazisi ile kullanicidan bir girdi alin. 
# Ardindan bu kullanici girişi ile rollDice yöntemini çağirin. 
# Son olarak, her olasiliği yazdirin. Örneğin. "0 olasiliği 16.20'dir"