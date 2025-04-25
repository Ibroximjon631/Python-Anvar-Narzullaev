ii=['Abc','Abc','iii','Iiii','Xyz',1,2,3]
while 'Abc' in ii:
    ii.remove('Abc')
print(ii)
while ii:
    del ii[0]
print(ii)