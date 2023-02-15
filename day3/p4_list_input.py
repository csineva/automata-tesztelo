print('************ 4. feladat ******************')
'''
Készíts egy öt elemű felhasználótól bekért törtszám listát! Jelenítsd meg a képernyőn a listát!
'''

inputlist = []

print('kérlek adj meg 5 törtszámot:')
for i in range(5):
    inputlist.append(input(f'{i + 1}. szám'))
print('A lista: ', inputlist)
