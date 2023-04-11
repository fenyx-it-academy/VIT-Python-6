
def rollDice(sayi):
    import random
    zar=[0,0,0,0,0,0]

    for i in range(sayi):
        x=random.randint(1, 6)
        zar[x-1]+=1
    
    zaratis=1
    for y in zar:
        yuzdelik=y*100/sum(zar)
        yuzdelik=round(yuzdelik,2)
        print(f'{zaratis} degerinin yuzdelik karsılıgı {yuzdelik}')
        zaratis+=1
        