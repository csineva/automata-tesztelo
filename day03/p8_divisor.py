print('************ 8. feladat ******************')
'''
Írj egy szkriptet, ami bekér a felhasználótól egy számot, majd írasd ki ennek a számnak az egész osztóit!
'''
szam = int(input('Kérek egy számot:'))
osztok = []
for i in range(1, szam//2 + 1):
    if szam % i == 0:
        print(i, ', ', sep="", end='')
print(szam)