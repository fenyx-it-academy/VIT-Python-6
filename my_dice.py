def rollDice(arg):
    import random

    zar = [0, 0, 0, 0, 0, 0]
    sayi = []
    for i in range(arg):
        sayiSec = random.randint(1, 6)
        sayi.append(sayiSec)
        sonuc = random.choice(sayi)
        # sayi.append(sonuc)
        # Asagidaki if statementlarin kisa yazimi bu sekildedir:
        zar[sayiSec-1] += 1
        # uzun hali...
        # if sonuc == 1:
        #     zar[0] += 1
        # elif sonuc == 2:
        #     zar[1] += 1
        # elif sonuc == 3:
        #     zar[2] += 1
        # elif sonuc == 4:
        #     zar[3] += 1
        # elif sonuc == 5:
        #     zar[4] += 1
        # elif sonuc == 6:
        #     zar[5] += 1
        # else:
        #     break
    print('Son atilan zarin numarasi: ', sonuc)
    # print('Her sayidan kac defa atilan zar listesi: ', sayi)
    print('Hangi numaradan kac defa atildiginin listesi: ', *zar)

# Listeyi yazdırmak yerine, yüzde listesini döndürür.
    yuzdeSonuc = []
    yuzde = 1
    for i in zar:
        sonucYuzdeOlarak = 100 * i / 5000
        sonucYuzdeOlarak = round(sonucYuzdeOlarak, 2)
        yuzdeSonuc.append(sonucYuzdeOlarak)
        print(f'{yuzde}: {sonucYuzdeOlarak}')
        yuzde += 1
    print(yuzdeSonuc)


# Fonksiyon, 5000 defa tekrar yerine, verilen sayı değişkeni kadar tekrar yapar.
rollDice(1)
