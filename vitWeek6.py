# # 1. Rastgele Sayi Tahmini

# # 1'den 100'e kadar rastgele bir tam sayi seçen bir program yaziniz. Programiniz kullanicidan tahminler istemelidir –
# # Eğer kullanici yanliş tahmin ederse, tahminin çok yüksek veya çok düşük olduğunu yazdirmalidir.
# # Kullanicinin geçerli girdi girip girmedigini kontrol etmeniz de gerekmektedir.
# # Kullanici doğru tahmin ederse, program kullanicinin doğru cevabi tahmin etmek için ne kadar zaman harcadiğini yazdirmalidir.

# import random # random ile rastgele sayi uretebiliyoruz
# import time # time fonksiyonu ile zaman hesaplamasi yapacagiz

# # programa baslangici icin sayac saymaya basliyor
# baslangic = time.time()

# # rastgele sayi sistem tarafindan uretiliyor
# sayiUret = random.randint(1, 100)

# # tahmini tutmasi icin degisken atiyoruz ve
# # en sonra bulmak icin hangi sayilari girmisiz gostemesi icin bos liste tutuyoruz
# tahmin = 0
# liste = []

# # donguye basliyoruz ki surekli soru sormaya devam etsin
# while True:
#     # try ve exception ile hata verirse istedigimiz gibi bir cikti vermesini sagliyoruz
#     try:
#         # kullanicidan tahminini aliyoruz
#         tahmin = int(input(
#             'Rastgele uretilen sayiyi bulmak icin Lutfen 1 den 100 e kadar bir sayi giriniz: '))
#         # tahminini bos listeye surekli olarak ekliyoruz
#         liste.append(tahmin)
#     #    if statement ile belirtilen araliklarda tahmin yapmasini ve kucuk buyuk yonlendirmesini yapiyoruz
#         if tahmin < 1 or tahmin > 100:
#             print(
#                 'Hatali bir giris yaptiniz. Lutfen 1 ile 100 arasinda bir deger giriniz!!! ❌')
#         elif sayiUret == tahmin:
#             print(
#                 f'Rastgele uretilen sayi: {sayiUret}, sizin tahmininiz {tahmin}. Tebrikler kazandiniz 🎉🎈✨')
#             break
#         elif sayiUret > tahmin:
#             print(
#                 f"Rastgele uretilen sayi sizin tahmininiz {tahmin}'den BUYUK, lutfen daha BUYUK 👆 bir sayi giriniz: ")
#         else:
#             print(
#                 f"Rastgele uretilen sayi sizin tahmininiz {tahmin}'den KUCUK, lutfen daha KUCUK 👇 bir sayi giriniz: ")
#     except ValueError:
#         print('Hatali bir giris yaptiniz. Lutfen 1 den 100 kadar bir sayi giriniz')

# # bitis ile programa baslarken baslayan sayaci durduruyoruz
# bitis = time.time()
# # sonuc saniyeyi hesaplayip yaklsik bir sn icin round ile yuvarliyoruz
# yuvarla = round(bitis - baslangic)
# # sonuclari ekrana yazdiriyoruz
# print(f'Yaklasik olarak {yuvarla} sn de buldunuz')
# print(f'Tum sectiginiz sayilarin listesi: {liste}')

################################################################

# 2. Zar Yüzdesi

# Zar adlı 6 öğeli bir liste oluşturun. Bu listeyi sıfır değeriyle doldurun. 5000
# kez tekrarlayarak 1 ile 6 arasında (tıpkı bir zar gibi) rastgele bir sayı oluşturun.

# Değer 1 ise, listedeki 0 öğesini 1 artırın, aynısı 2, 3, 4, 5 ve 6 değerleri
# için de geçerlidir. dice[0] öğesi, 1 değerinin kaç kez oluştuğunu gösterir. Veya
# genel olarak: zar[x-1], x'in kaç kez atıldığını gösterir.

# Tekrarın sonunda, listenin içeriğini 2 ondalık basamakla yüzde olarak yazdırın.
# Örneğin; "3 değerindeki atışların yüzdesi = %16,28"
from my_dice import rollDice

yuzdeSonuc = rollDice()
rollDice()
