# 3. Basic Import
# my_dice.py adlı bir Python modülü oluşturun ve 2. soruda yazdığınız kodu rollDice(sayı) adlı bir fonksiyona aktarın.
def rollDice(sayi):
    import random
    Zar = [0, 0, 0, 0, 0, 0]
    try:
        sayi = int(sayi)
        for _ in range(sayi):
            i = random.randint(1, 6)
            Zar[i-1] += 1
        Rakam = 0
        Yuzdeler = ""
        for j in Zar:
            Rakam += 1
            Yuzde = (j / sum(Zar))*100
            Yuzdeler += "{} degerindeki atislarin yuzdesi = %{:.2f} _".format(
                Rakam, Yuzde)
        return Yuzdeler
    except ValueError:
        print("Lutfen bir sayi giriniz.")


# Değişiklikler:
# Fonksiyon, 5000 defa tekrar yerine, verilen sayı değişkeni kadar tekrar yapar. Listeyi yazdırmak yerine, yüzde listesini döndürür.

# Ardından main.py adlı yeni bir modül oluşturun. "Tekrar numarasını girin:" yazisi ile kullanıcıdan bir girdi alin.
# Ardından bu kullanıcı girişi ile rollDice yöntemini çağırın. Son olarak, her olasılığı yazdırın. Örneğin. "0 olasılığı 16.20'dir"
