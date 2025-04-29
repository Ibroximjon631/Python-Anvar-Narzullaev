import random as ii
from curses.ascii import isascii, isalpha

wds=['abc','xyz','ibroximjon','kimdr']
bitta=ii.choice(wds)
iii=len(bitta)
entr=[]
abc = ["_" for _ in bitta]
cnt=0
cnti=0
abcii=[]
while True:
    cnti+=1
    harf=(input(f"{"".join(abc)}. {iii} ta so'z oyladm. Harf kiriting:"))
    entr.append(harf)
    print(f"Sz kiritgan harflar:{"".join(entr).capitalize()}")
    if harf.isascii() and harf.isalpha() and len(harf)==1:
        if harf.lower() in bitta:
                for i in range(iii):
                    if bitta[i]==harf.lower():
                        abcii.append(harf.lower())
                        abc[i]=harf
                        cnt+=1
                        if abcii.count(harf.lower())>bitta.count(harf.lower()):
                            cnt-=1
                            break




                if cnt==iii:
                    print(f"Soz {bitta} edi. {cnti}")
                    break
    else:
        print("Notogri narsa kirityapsiz")