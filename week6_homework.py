# 1. Rastgele Sayi Tahmini

# 1'den 100'e kadar rastgele bir tam sayı seçen bir program yazınız. Programınız kullanıcıdan tahminler istemelidir – 
# eğer kullanıcı yanlış tahmin ederse, tahminin çok yüksek veya çok düşük olduğunu yazdırmalıdır.
# Kullanıcı doğru tahmin ederse, program kullanıcının doğru cevabı tahmin etmek için ne kadar zaman harcadığını yazdırmalıdır. 
# Kullanıcının geçerli girdi girip girmedigini kontrol etmeniz de gerekmektedir.

import random,timeit

number = random.randint(1,100)
print(number)
start = timeit.default_timer()
while True:
    try:
        
        mynum = int(input("Enter a number :"))
        if mynum < 0 or mynum > 100:
            raise ArithmeticError("Please enter a number between 0 and 100")
        elif mynum > number:
            print("Down")
        elif mynum < number:
            print("Up")
        else:
            print("Congratulations....")
            break
    except ArithmeticError as e:
        print(e)
    except ValueError :
        print("Please enter a NUMBER !!")
end = timeit.default_timer()
print(f"{number} of number {round(end-start)}sec founded .")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Zar Yüzdesi
# Zar adlı 6 öğeli bir liste oluşturun. Bu listeyi sıfır değeriyle doldurun. 5000 kez tekrarlayarak 1 ile 6 arasında (tıpkı bir zar gibi) rastgele bir sayı oluşturun.
# Değer 1 ise, listedeki 0 öğesini 1 artırın, aynısı 2, 3, 4, 5 ve 6 değerleri için de geçerlidir. dice[0] öğesi, 1 değerinin kaç kez oluştuğunu gösterir. 
# Veya genel olarak: zar[x-1], x'in kaç kez atıldığını gösterir.
# Tekrarın sonunda, listenin içeriğini 2 ondalık basamakla yüzde olarak yazdırın. Örneğin; "3 değerindeki atışların yüzdesi = %16,28"

import random

dice = [0,0,0,0,0,0]

for i in range(5000):
    dice[random.randint(0,5)] += 1
    
print (dice)

for i in range(0,6):
    dice[i] = ((dice[i]/5000)*100)

    print(f" {i+1} değerindeki atışların yüzdesi = % {dice[i]:.2f}")
print(dice)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------




