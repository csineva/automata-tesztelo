import random

print('************ 13. feladat ******************')
'''
Írj egy kő - papír - olló játékot!
Két játékos egymás után választhat, a szokásos szabályok mentén.
Írd ki, hogy melyik játékos nyert, illetve, hogy szeretnék-e tovább folytatni a játékot?
'''

list = ['Kő', 'Papír', 'Olló']
Player1 = input ('Egyik játékos neve: ') or "Viktor"
Player2 = input ('Másik játékos neve: ') or "Ferenc"

while True:
    print()
    go = input('Mehet: Enter \nKilépés: "exit"')
    print()
    if go.lower() == 'exit':
        break

    roll1 = random.choice(list)
    print(f'{Player1}: {roll1}')

    roll2 = random.choice(list)
    print(f'{Player2}: {roll2}')

    if roll1 == roll2:
        print('Egál')
        continue

    if roll1 == 'Kő' and roll2 == "Olló":
            print(Player1, 'nyert!')
    elif roll1 == 'Papír' and roll2 == "Kő":
            print(Player1, 'nyert!')
    elif roll1 == 'Olló' and roll2 == "Papír":
            print(Player1, 'nyert!')
    else:
        print(Player2, 'nyert!')