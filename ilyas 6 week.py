#1.Sorunun Cevabı
#---------------------
import random         #rasgele sayı seçtirmek için random modülünü import ettik
import time            #geçen süreyi hesaplamak için time modülünü import ettik
tsayi=random.randint(1, 100)    #1 ile 100 arasında bilgisayar bir sayı tutmasını sağladım
tahmin=0  
basla=time.time()    #zamanı hesaplamak için bu satırda zamanın başlangıcını değişkene atadım
while True:
    try:                 #hata ayıklama yapacağımız içim try ile başadım
        tahmin=int(input('Lütfen 1 ile 100 arasında bir sayı giriniz'))
        if (type(tahmin) != int) or (tahmin not in range(1,101)):          #girilen sayının 1 ile 100 arasında olup olamdığını ve tamsayı durumunukontrol edip eğer degilse raise komutu ile hata olusturduk  
            raise ValueError()
        if tahmin>tsayi:
            print('Lütfen küçük bir sayı giriniz')            #if komutu ile gerekli kontrolü sağladım
        
        elif tahmin<tsayi:
            print('Lütfen büyük bir sayı giriniz')
        
        else:
            bitir=round((time.time()-basla),1)         #programın bitis zamanı için bu satırda basalngıc ile bitis arasındaki farkı aldık
            print(f'Tebrikler tutulan  {tsayi} sayıyısını  {bitir} saniyede buldunuz')
            break
    except ValueError:
        print(ValueError("Lütfen geçerli bir sayı giriniz"))      #eger farklı bir giriş yapılırsa kullanıcıya tekrar denemesi için hata mesajı yazdırıldı.
        
#2.Sorunun Cevabı  
import random
zar=[0,0,0,0,0,0]

for i in range(5000):
    x=random.randint(1, 6)
    zar[x-1]+=1
    
zaratis=1
for y in zar:
    yuzdelik=y*100/sum(zar)
    yuzdelik=round(yuzdelik,2)
    print(f'{zaratis} degerinin yuzdelik karsılıgı {yuzdelik}')
    zaratis+=1
    
    
  #Diğer sorunun cevabı dosya olarak eklendi.


