"""
1. Rastgele Sayi Tahmini
1'den 100'e kadar rastgele bir tam sayı seçen bir program yazınız. Programınız kullanıcıdan tahminler istemelidir – 
eğer kullanıcı yanlış tahmin ederse, tahminin çok yüksek veya çok düşük olduğunu yazdırmalıdır. 
Kullanıcı doğru tahmin ederse, program kullanıcının doğru cevabı tahmin etmek için ne kadar zaman harcadığını yazdırmalıdır.
Kullanıcının geçerli girdi girip girmedigini kontrol etmeniz de gerekmektedir.
"""

import random
import time

def validate_input(user_input):
    try:
        guess = int(user_input) #guess --> tahmin etmek
        if guess < 1 or guess > 100:
            return -1 # 1 ile 100 arasinda degil
        else:
            return 0 # gecerli input
    except:
        return -2 # integer degil

def main():
    random_number = random.randint(1, 100)
    print(random_number)
    guess = None
    num_guesses = 0
    while guess != random_number:
        user_input = input("Tahmin et (1-100): ")
        input_status = validate_input(user_input)
        if input_status == -2:
            print("Geçersiz giriş. Lütfen bir tamsayı girin.")
        elif input_status == -1:
            print("Geçersiz giriş. Lütfen 1 ile 100 arasında bir sayı girin.")
        else:
            guess = int(user_input)
            num_guesses += 1
            if guess < random_number:
                print("Çok düşük.")
            elif guess > random_number:
                print("Çok yüksek.")
            else:
                print("Tebrikler! Doğru sayıyı tahmin ettiniz.")
                print("Tahmin etmek için harcanan zaman: {} saniye".format(time.process_time()))
                print("Tahmin sayısı: {}".format(num_guesses))
    
if __name__ == "__main__":
    main()
    



"""
2. Zar Yüzdesi
Zar adlı 6 öğeli bir liste oluşturun. Bu listeyi sıfır değeriyle doldurun. 5000 kez tekrarlayarak 1 ile 6 arasında (tıpkı bir zar gibi) 
rastgele bir sayı oluşturun.

Değer 1 ise, listedeki 0 öğesini 1 artırın, aynısı 2, 3, 4, 5 ve 6 değerleri için de geçerlidir. dice[0] öğesi, 
1 değerinin kaç kez oluştuğunu gösterir. 
Veya genel olarak: zar[x-1], x'in kaç kez atıldığını gösterir.

Tekrarın sonunda, listenin içeriğini 2 ondalık basamakla yüzde olarak yazdırın. Örneğin; "3 değerindeki atışların yüzdesi = %16,28"
"""
import random


dices = {1:0,2:0,3:0,4:0,5:0,6:0}  #zar=dice
for i in range(5000):
    dice =( random.randint(1,6))
    dices[dice]+=1
for dice in dices :
    print(f"{dice} sayisinin gelme olasiligi : {dices[dice]/5000} 'dir. ") 
    print(f"{dice} sayisi {dices[dice]} defe geldi.") 
    print("**********") 
   
