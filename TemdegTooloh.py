a=input('temdegt mur oruul ')
sum=0
for x in range(0, len(a)):
    if not('A'<=a[x] and a[x]<='Z') and not(a[x]>='a' and a[x]<='z') and not('0'<=a[x] and a[x]<='9'):
        sum=sum+1
print('Useg bolon tsifr bish temdegtiin too - ', sum)
