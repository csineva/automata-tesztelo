print('************ 9. feladat ******************')
'''
Készíts egy szkriptet, ami kiírja a képrenyőre, hogy a felhasználótól bekért szám páros vagy páratlan?
'''

while True:
    getnr = input('Kérek egy számot (vagy "exit" a kilépéshez):')
    if getnr.lower() == 'exit':
        break
    elif int(getnr) % 2 == 0:
        print('páros')
    else:
        print('páratlan')