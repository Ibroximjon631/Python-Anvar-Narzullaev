import random as iii

print('Game')
Abc=1
iiii=0
number=iii.randint(1,10)
while Abc:
    iiii+=1
    ii=int(input('Necini oyladm(1dan 10gaca)?:'))
    
    if number==ii:
        print(f"To'gri Men oylagan number {number} edi.{iiii}")
        break
    elif number>ii:
        print("Katta")
        continue
    else:
        print('Kicik')

print("1 dan 10gaca o'ylang")
abc=input("Boshlash ucun bron nimani bosing.")
start=1
ohiri=10
Iiiiii=0
while True:
    Iiiiii+=1
    numberi=iii.randint(start,ohiri)
    abcdef=input(f"Togri bosa : Abc kirit , Numberdan kicik bosa: Iii , Katta bosa : Xyz. {numberi}")
    if abcdef=='Abc':
        print(f"Ha ha ha {Iiiiii}ta")
        kyn=input("Oynismi?")
        if kyn=='Ha':
            start=1
            ohiri=10
            Iiiiii=0
            continue
        else:
            break
    elif abcdef=='Iii':
        ohiri=numberi-1
    else:
        start=numberi+1
