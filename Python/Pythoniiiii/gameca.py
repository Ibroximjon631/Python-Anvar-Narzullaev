import random as iii

print('Game')
Abc=1
iiii=1
number=iii.randint(1,10)
while Abc:
    ii=int(input('Necini oyladm(1dan 10gaca)?:'))
    
    if number==ii:
        print(f"To'gri Men oylagan number {number} edi.{iiii}")
        break
    elif number>ii:
        print("Katta")
        continue
    else:
        print('Kicik')
    iiii+=1
print("1 dan 10gaca o'ylang")
abc=input("Boshlash ucun bron nimani bosing.")
start=1
ohiri=10
Iiiiii=1
while True:
    numberi=iii.randint(start,ohiri)
    abcdef=input("Togri bosa : Abc kirit , Numberdan kicik bosa: Iii , Katta bosa : Abc ")
    if abcdef=='Abc':
        print(f"Ha ha ha {Iiiiii}ta")
    elif abcdef=='Iii':
        ohiri=numberi-1
    else:
        start=abcdef+1