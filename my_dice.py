# ## 3. Basic Import

# my_dice.py adli bir Python modülü oluşturun ve 2. soruda yazdiğiniz kodu rollDice(sayi) adli bir fonksiyona aktarin.
# Fonksiyon, 5000 defa tekrar yerine, verilen sayi değişkeni kadar tekrar yapar.
# Listeyi yazdirmak yerine, yüzde listesini döndürür.
# Ardindan main.py adli yeni bir modül oluşturun. 
# "Tekrar numarasini girin:" yazisi ile kullanicidan bir girdi alin. 
# Ardindan bu kullanici girişi ile rollDice yöntemini çağirin. 
# Son olarak, her olasiliği yazdirin. Örneğin. "0 olasiliği 16.20'dir"
import random

def rollDice(num):
    dice = [0, 0, 0, 0, 0, 0]

    for i in range(num):
        roll = random.randint(1, 6)
        dice[roll-1] += 1

    percentages = []
    for i in range(6):
        percentage = (dice[i] / num) * 100
        percentages.append(percentage)
    
    return percentages
