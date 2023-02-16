print('************ 10. feladat ******************')
'''
Adott egy lista számokkal: 15, 56, 1, 89, 2, 78, 9, 40, 10, 32.
I. Írasd ki egyesével a képernyőre, egymás alá a 10-nél kisebb számokat!
II. Gyűjtsd egy listába a 20-nál nagyobb számokat! Jelenítsd meg a listaelemeket és hogy hány elemű ez a lista!
III. Növekvő sorrendben írasd ki a számokat egyesével, egy sorba!
'''
mylist = [15, 56, 1, 89, 2, 78, 9, 40, 10, 32]
twenty = []
for i in mylist:
    if i < 10:
        print(i)


for i in mylist:
    if i > 20:
        twenty.append(i)
print(twenty, 'length: ', len(twenty))


for i in sorted(mylist):
    print(i)




