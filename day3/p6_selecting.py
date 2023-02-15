print('************ 6. feladat ******************')
'''
Adott egy lista, mely számokat tartalmaz. Jelenítsd meg a listából azokat a számokat a képernyőn, melyek oszthatók öttel. 
Viszont, ha a szám nagyobb mint 100, akkor, azt hagyd figyelmen kívül és lépj a következő számra.
Ha 250-nél is nagyobb a szám, fejezd be a kiíratást.
A számok: 8, 10, 75, 149, 64, 89, 225, 5, 145, 260, 1, 50
'''

l = [8, 10, 75, 149, 64, 89, 225, 5, 145, 260, 1, 50]

for i in range(len(l)):
    if l[i] > 250:
        break
    elif l[i] > 100:
        continue
    elif l[i] % 5 == 0:
        print(l[i])

