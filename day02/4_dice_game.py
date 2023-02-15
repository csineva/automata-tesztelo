"""---------------------------------------------------------------------------------------------------------------------
4. feladat
Szimuláljunk le egy kocka dobás játékot.
Minden körben a gép és a játékos is kap egy véletlenszerű értéket 1 és 6 között.
Az nyeri az adott fordulót, aki nagyobbat dobott.
Ha ugyanakkorát dobtunk, akkor újra dobunk.
A játék 5 győzelemig tart. Aki előbb eléri az 5 körgyőzelmet, az lesz a nyertes.
"""

# 4. feladat megoldása jöhet ide
import random
import time

rounds = 2
human_win = 0
machine_win = 0
human = input("kérlek add meg a neved: ") or 'Human'
machine = "Deus Ex"

print(f'''Kedves {human} és {machine}, indul a mérkőzés!
A játék öt körgyőzelemig megy, a nagyobb szám nyeri a kört.
Egyenlő számok esetén a játékosok újra gurítanank.
''')
while human_win < rounds and machine_win < rounds:
    print('-' * 40)
    wait = input(f'Kedves {human} nyomj Entert a gurításhoz!')

    human_rolling = random.randint(1, 6)
    print(f'{human} gurítása: {human_rolling}')
    print(f'{machine} is rázogatja a kockát:')
    time.sleep(2)

    machine_rolling = random.randint(1, 6)
    print(f'{machine} gurítása: {machine_rolling}')
    time.sleep(1)
    print()

    if human_rolling > machine_rolling:
        print(f'A kört {human} nyerte!')
        human_win += 1
        print(f'Eredmény: \n{human} {human_win} : {machine} {machine_win}')
    elif human_rolling < machine_rolling:
        print(f'A kört {machine} nyerte!')
        machine_win += 1
        print(f'Eredmény: \n{human} {human_win} : {machine} {machine_win}')
    else:
        print('Döntetlen! A játékosok újra gurítanak')
        print(f'Eredmény: \n{human} {human_win} : {machine} {machine_win}')
print()
print('-' * 30)
print('-' * 30)
print(f'Végeredmény: \n{human} {human_win} : {machine} {machine_win}')
print('-' * 30)
print('-' * 30)
