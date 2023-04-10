# Rastgele Sayi Tahmini

import random
import time

start = time.time()
computer = random.choice(range(1,101))

while True:
  try:
    number = int(input("Please enter a number between 0 and 100: "))
    if (type(number) != int) or (number not in range(1,101)):
            raise ValueError("Please make sure you enter a number")
        
    if 100>=number>=1:
        
      if number>computer:
        print(f"{number} is higher than the computer's choice!")
        
      elif computer>number:
        print(f"{number} is lower than the computer's choice!")
        
      else:
        elapsed = time.time() - start
        print("Your guess is correct")
        break  
    
    else:
      print("You did not enter a number between 0 and 100!")

  except ValueError as e:
    print(f"TypeError: {e}")
    
print(f"The program has been successfully terminated and you guessed it in {elapsed} time")

# Zar Yüzdesi
# Zar adlı 6 öğeli bir liste oluşturun. Bu listeyi sıfır değeriyle doldurun. 
# 5000 kez tekrarlayarak 1 ile 6 arasında (tıpkı bir zar gibi) rastgele bir sayı oluşturun.

# Değer 1 ise, listedeki 0 öğesini 1 artırın, aynısı 2, 3, 4, 5 ve 6 değerleri için de geçerlidir. 
# dice[0] öğesi, 1 değerinin kaç kez oluştuğunu gösterir. Veya genel olarak: zar[x-1], x'in kaç kez atıldığını gösterir.  
# Tekrarın sonunda, listenin içeriğini 2 ondalık basamakla yüzde olarak yazdırın. 
# Örneğin; "3 değerindeki atışların yüzdesi = %16,28"

import random
zar = [0, 0, 0, 0, 0, 0]

for i in range(5000):
  x = random.randint(1,6)
  zar[x-1] += 1

dice = 1
for i in zar:
  yuzde = i * 100 / sum(zar)
  yuzde = round(yuzde, 2)
  print(f"{dice} değerindeki atışların yüzdesi: {yuzde}")
  dice +=1
  
# Basic Import
# my_dice.py adlı bir Python modülü oluşturun ve 2. soruda yazdığınız kodu rollDice(sayı) adlı bir fonksiyona aktarın.

# Değişiklikler:
# Fonksiyon, 5000 defa tekrar yerine, verilen sayı değişkeni kadar tekrar yapar. 
# Listeyi yazdırmak yerine, yüzde listesini döndürür.

def rollDice(sayi):  
    import random
    zar = [0, 0, 0, 0, 0, 0]
    try:
        if (type(sayi) != int) or sayi <= 0:
            raise ValueError("Only integers are allowed")
        for i in range(sayi):
            x = random.randint(1,6)
            zar[x-1] += 1

        dice = 1
        for i in zar:
            yuzde = i * 100 / sum(zar)
            yuzde = round(yuzde, 2)
            print(f"{dice} değerindeki atişlarin yüzdesi: {yuzde}")
            dice +=1
            
    except ValueError as e:
        return f"{e}"
      
# Ardından main.py adlı yeni bir modül oluşturun. 
# "Tekrar numarasını girin:" yazisi ile kullanıcıdan bir girdi alin. 
# Ardından bu kullanıcı girişi ile rollDice yöntemini çağırın. 
# Son olarak, her olasılığı yazdırın. Örneğin. "0 olasılığı 16.20'dir" 

import my_dice

number = input("Please enter how many times you want to roll the dice: ")

try:
    if not int(number) > 0:
        raise ValueError("Only integers are allowed")
    
    result = my_dice.rollDice(int(number))
    
except ValueError as e:
    print(f"Type Error: {e}")

else:
    print(result)      