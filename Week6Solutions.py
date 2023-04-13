#<!-- # VIT-Python-6

## 1. Rastgele Sayi Tahmini

#1'den 100'e kadar rastgele bir tam sayi seçen bir program yaziniz.
# Programiniz kullanicidan tahminler istemelidir – eğer kullanici yanliş tahmin ederse, tahminin çok yüksek veya çok düşük olduğunu yazdirmalidir. 
# Kullanici doğru tahmin ederse, program kullanicinin doğru cevabi tahmin etmek için ne kadar zaman harcadiğini yazdirmalidir. 
# Kullanicinin geçerli girdi girip girmedigini kontrol etmeniz de gerekmektedir.

import random
from datetime import datetime

# Rastgele bir sayi seçin
num = random.randint(1, 100)

# Başlangiç zamanini kaydedin
start_time = datetime.now()

# Kullanicinin tahminlerini isteyin
guess = None
while guess != num:
    try:
        guess = int(input("1 ile 100 arasinda bir sayi tahmin edin: "))
    except ValueError:
        print("Geçerli bir sayi girin.")
        continue
    
    if guess < num:
        print("Tahmininiz çok düşük.")
    elif guess > num:
        print("Tahmininiz çok yüksek.")

# Bitiş zamanini kaydedin ve geçen süreyi hesaplayin
end_time = datetime.now()
time_elapsed = end_time - start_time

print("Doğru tahmini {0} saniyede yaptiniz.".format(time_elapsed.total_seconds()))


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


