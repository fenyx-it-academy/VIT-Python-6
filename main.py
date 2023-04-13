# ## 3. Basic Import

# my_dice.py adli bir Python modülü oluşturun ve 2. soruda yazdiğiniz kodu rollDice(sayi) adli bir fonksiyona aktarin.
# Fonksiyon, 5000 defa tekrar yerine, verilen sayi değişkeni kadar tekrar yapar.
# Listeyi yazdirmak yerine, yüzde listesini döndürür.
# Ardindan main.py adli yeni bir modül oluşturun. 
# "Tekrar numarasini girin:" yazisi ile kullanicidan bir girdi alin. 
# Ardindan bu kullanici girişi ile rollDice yöntemini çağirin. 
# Son olarak, her olasiliği yazdirin. Örneğin. "0 olasiliği 16.20'dir"

from my_dice import rollDice

num = int(input("Tekrar numarasini girin: "))
percentages = rollDice(num)

for i in range(6):
        print("{} olasiliği {:.2f}'dir".format(i+1, percentages[i]))