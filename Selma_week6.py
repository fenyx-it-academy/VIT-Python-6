#cevap1
import random
import time 


sayi=random.randint(1, 100)
print("\n1-100 arasında bir sayı seçildi. Tahmin etmeye başla!")

baslangic=time.time()

while True:
    try:
      tahmin = int(input("\nTahmininiz: "))
      if tahmin<sayi:
          print("Çok düşük. Daha yuksek bir sayi deneyin.")
      elif tahmin>sayi:
          print("Çok yüksek. Daha kucuk bir sayi deneyin.")
      else:
          bitis=time.time()-baslangic
          print(f"Tebrikler! {sayi} sayısını toplam {bitis} saniyede bildiniz.")
          break
    except:
        print("Lütfen geçerli bir tam sayı girin.")


        
#cevap2
import random
zar = [0] * 6

for i in range(5000):
    sayi = random.randint(1, 6)
    zar[sayi-1] += 1

dice = 1
for i in zar:
  yuzde = i * 100 / sum(zar)
  yuzde = round(yuzde, 2)
  print(f"{dice} değerindeki atışların yüzdesi: {yuzde}")
  dice +=1


#cevap3

def rollDice(sayi):
    import random
    zar[0]*6
for i in range(sayi):
    sayi = random.randint(1, 6)
    zar[sayi-1] += 1

dice = 1
for i in zar:
    yuzde = i * 100 / sum(zar)
    yuzde = round(yuzde, 2)
    print(f"{dice} değerindeki atışların yüzdesi: {yuzde}")
dice +=1



import my_dice

num = int(input("Tekrar numarasını girin: "))

percentages = my_dice.rollDice(num)

for i in range(6):
    print(f"{i+1} olasılığı %{percentages[i]:.2f}")
 

    

    
