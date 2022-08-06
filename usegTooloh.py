b=['a', 'e', 'i', 'u', 'o']
a=input('ug oruul ')
counter = 0
for x in range(0, len(a), 1):
    if a[x] in b:
        counter+=1
print(counter)
