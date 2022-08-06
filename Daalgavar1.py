a=input('Temdegt mur oruul ')
b=''
for x in range(len(a)-1, -1, -1):
    b=b+a[x]
print(b)
if b == a:
    print('Mun')
else: print('Bish')
