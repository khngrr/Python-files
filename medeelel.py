name = []
age = []
phone = []
reg = []
for x in range(1, 3):
    print(x,'-r hunii medeelel oruul')
    name.append(input('neriig oruul '))
    age.append(input('nasiig oruul '))
    phone.append(input('utasiig oruul '))
    reg.append(input('registeriig oruul '))
print('nereer haih bol n dar \\ utasaar haih bol u dar')
a=input('songoltoo oruul ')
if a == 'n':
    b=input('haih neriig oruul ')
    if b in name:
        d=name.index(b)
        print('ene hunii utas', phone[d])
        print('ene hunii register', reg[d])
    else: print('tiim nertei hunii medeelel baihgui')
if a == 'u':
    b = input('haih utasiig oruul ')
    if b in phone:
        d = phone.index(b)
        print('ene hunii ner', name[d])
        print('ene hunii register', reg[d])
    else: print('tiim utastai hunii medeelel baihgui')
