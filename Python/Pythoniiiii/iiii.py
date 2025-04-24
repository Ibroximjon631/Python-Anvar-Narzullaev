# nimadr={
#     'name':'Ibroximjon', 
#     'iii':'20'
#     }
# print(nimadr['name'],nimadr['iii'])


# nimadr['iiii']='Abc'
# nimadr['name']='Muhammad ali'
# print(nimadr)
# print(type(nimadr))


# del nimadr["iii"]
# print(nimadr)


# print(nimadr.get("namei", "Yoq")) #If Bor birincisi, Else : ___
# print(nimadr.get("namei")) # Else Yoq : None 


iiii={
    'name':'Ali',
    'age':20 
    }

iiii['name123']='Ibroximjon'
print(iiii)
iiii['name']='Muhammad Ali'
print(iiii)
del iiii['age']
print(iiii)
print(iiii.get('name12345',"Yo'q"))
print(iiii)