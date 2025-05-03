with open('iiii.txt') as fd:
    ii=fd.read()
print(ii)
ii=ii.rstrip()
ii=ii.replace(' ','')
print(ii)
print(type(ii))