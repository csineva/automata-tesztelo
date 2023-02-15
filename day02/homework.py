# KEEP IT SIMPLE :)

"""
1. feladat
Kérjünk be a felhasználótól folyamatosan szövegeket, amíg 'exit' utasítást nem ad meg.
- Írassuk ki egy sorban az aktuálisan megkapott szöveget, egy nyilat és a szöveget visszafelé.
  Pl.: toyota --> atoyot
- Az 'exit' parancs érkezhet bármilyen formában. Pl.
  eXit, EXIT, EXiT stb.
  Oldjuk meg ezt a problémát.
- Kilépéskor köszönjön el a program.
"""
import random
import time

# 1. feladat megoldása jöhet ide

# print('1. feladat')
# print()
#
# exit_string = False
# print('Kérlek írj be néhány szót (kilépéshez: exit)')
#
# while not exit_string:
#     user_string = input()
#     if user_string.lower() == 'exit':
#         print("Köszi a játékot! Szia! :)")
#         exit_string = True
#     else:
#         reversed_string = user_string[::-1]
#         print(user_string, '--->', reversed_string)


# Extended version (with palindrome check)

# print('Rendezői változat')
# print()
#
# exit_string = False
# print('Kérlek írj be néhány szót (kilépéshez: exit)')
#
# while not exit_string:
#     user_string = input()
#     check_palindrom = user_string.replace(' ', '').lower()
#
#     if user_string.lower() == 'exit':
#         print("Köszi a játékot! :)")
#         exit_string = True
#     elif check_palindrom == check_palindrom[::-1]:
#         print(user_string, "<--->", user_string, "\nNahát! Ez egy palindrom!")
#     else:
#         reversed_string = user_string[::-1]
#         print(user_string, '--->', reversed_string)


"""---------------------------------------------------------------------------------------------------------------------
2. feladat
Kérdezzük meg a felhasználót, hogy hány számot szeretne megadni.
For ciklus segítségével kérjünk be annyi db számot, amennyit a felhasználó előzőleg meghatározott
és tároljuk őket egy listában.

Kimenetként
- Írassuk ki a teljes listát
- Írassuk ki a listát úgy, hogy csak minden 2. elemet tartalmazza.
- Rendezzük csökkenő sorrendbe a listát
"""

# 2. feladat megoldása jöhet ide

# numbers = []
# alma = []
# nr_of_numbers = int(input('Hány számot szeretnél megadni?'))
# print(f'Kérlek írd be egyenként ezt az {nr_of_numbers} számot:')
#
# for number in range(nr_of_numbers):
#     numbers.append(int(input(f'{number + 1}. szám: ')))
#
# print(f'A következő számokat adtad meg: {numbers}')
# print(f'Minden második szám: {numbers[1::2]}')
# numbers.sort(reverse=True)
# print(f'A számaid csökkenő sorrendben: {sorted(numbers, reverse=True)}')

# str.sort() sorba rendezést miért nem lehet változóba menteni?


"""---------------------------------------------------------------------------------------------------------------------
3. feladat 
Kérjünk be neveket a felhasználótól és tároljuk őket egy listában.
Minden név felvétel után kérdezzük meg, hogy akar-e még nevet felvenni.
Ha igen --> ismételjük az előzőeket
Ha nem --> kérdezzük meg, hogy csökkenő vagy növekvő sorrendben szeretné-e látni a névsort.
Írassuk ki a névsort a kért módon.
"""

# 3. feladat megoldása jöhet ide

# namelist = []
# exitstring = False
#
# print("Kérlek adj meg egy nevet: ")
# while not exitstring:
#     namelist.append(input())
#     more_name = input('Szeretnél még neveket felvenni? (igen: y, nem: bármely más billentyű)')
#     if more_name == 'y':
#         print("Kérlek adj meg még egy nevet!")
#     else:
#         exitstring = True
#
# order = input('Növekvő (n) vagy csökkenő (bármely más billentyű) sorrendbe rendezzem a neveket?')
# if order == 'n':
#     print(sorted(namelist))
# else:
#     print(sorted(namelist, reverse=True))



"""---------------------------------------------------------------------------------------------------------------------
4. feladat
Szimuláljunk le egy kocka dobás játékot.
Minden körben a gép és a játékos is kap egy véletlenszerű értéket 1 és 6 között.
Az nyeri az adott fordulót, aki nagyobbat dobott.
Ha ugyanakkorát dobtunk, akkor újra dobunk.
A játék 5 győzelemig tart. Aki előbb eléri az 5 körgyőzelmet, az lesz a nyertes.
"""

# 4. feladat megoldása jöhet ide

# rounds = 2
# human_win = 0
# machine_win = 0
# human = "Ágnes" #input("kérlek add meg a neved: ")
# machine = "Deus Ex"
#
# print(f'''Kedves {human} és {machine}, indul a mérkőzés!
# A játék öt körgyőzelemig megy, a nagyobb szám nyeri a kört.
# Egyenlő számok esetén a játékosok újra gurítanank.
# ''')
# while human_win < rounds and machine_win < rounds:
#     print('-' * 30)
#     wait = input(f'Kedves {human} nyomj Entert a gurításhoz!')
#
#     human_rolling = random.randint(1, 6)
#     print(f'{human} gurítása: {human_rolling}')
#     print(f'{machine} is rázogatja a kockát:')
#     time.sleep(2)
#
#     machine_rolling = random.randint(1, 6)
#     print(f'{machine} gurítása: {machine_rolling}')
#     time.sleep(1)
#     print()
#
#     if human_rolling > machine_rolling:
#         print(f'A kört {human} nyerte!')
#         human_win += 1
#         print(f'Eredmény: \n{human} {human_win} : {machine} {machine_win}')
#     elif human_rolling < machine_rolling:
#         print(f'A kört {machine} nyerte!')
#         machine_win += 1
#         print(f'Eredmény: \n{human} {human_win} : {machine} {machine_win}')
#     else:
#         print('Döntetlen! A játékosok újra gurítanak')
#         print(f'Eredmény: \n{human} {human_win} : {machine} {machine_win}')
# print()
# print('-' * 35)
# print('-' * 35)
# print(f'Végeredmény: \n{human} {human_win} : {machine} {machine_win}')
# print('-' * 35)
# print('-' * 35)

"""---------------------------------------------------------------------------------------------------------------------
SZORGALMI
A megadott stringben keressük meg az összes 'sör' előfordulást és tároljuk el az indexüket egy listában
"""

sentence = 'Egy sör nem sör. 2 sör fél sör. 4 sör 1 sör. 1 sör meg nem sör...'
sorindexek = []
vege = False
pointer = 0

while not vege:
    pointer = sentence.find('sör',pointer)
    if pointer > -1:
        sorindexek.append(pointer)
        print('Hoppá! Nicsak, itt is egy sör:', pointer)
        pointer += 1

        time.sleep(.5)
    else:
        vege = True

print('Sörökkévalóság!', sorindexek)