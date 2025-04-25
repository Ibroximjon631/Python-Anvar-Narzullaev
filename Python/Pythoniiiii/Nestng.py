# iii={
#     'name':'Ali',
#     'age':20 
#     }

# abcd={
#     'name':'Ibroximjon',
#     'age':20,
#     'kimdr':'Ibroximjon'
# }
# nimadr=[iii,abcd]
# for i in nimadr:
#     print(i['name'])






# print(nimadr[1]['kimdr'])




# iii=[]
# for i in range(1,5):
#     kimdrla={
#         'name':'Ali',
#         'kimdr': 'Ibroximjon',
#         'age':7
#     }
#     iii.append(kimdrla)
# for abcd in iii[:3]:
#     abcd['kimdr']='Muhammad Ali'
# print(iii)








iiii={
    'ali':{
        'name':'Ali',
        'kimdr':'Ibroximjon',   
        'abcd' : ['python','c']
        
    },
    'ibroximjon':{
        'name':'Ibroximjon',
        'kimdr':'Ali',
        'abcd' : ['python','c']
    }}

for i,ii in iiii.items():
    print(f"{i}",ii['name'],ii['kimdr'])
    for iiii in ii['abcd']:
        print(iiii, end=' ')