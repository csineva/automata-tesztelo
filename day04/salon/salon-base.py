# AUTÓ SZALON - KIINDULÓ VÁLTOZAT
# Példa kód a függvényesítéshez, modularizálás témakörhöz

# SETTINGS, DATA--------------------------------------------------------------------------------------------------------

EMPLOYEES = [
    ['Thomas', 42], # Név, életkor
    ['Jenny', 27]
]

CARS = [
    ['Ford Focus', 2007, True], # Név, gyártási év, benzines-e
    ['Kia Rio', 2014, False]
]

# PROGRAM---------------------------------------------------------------------------------------------------------------

print('Üdvözüljük kereskedés menedzsment eszközünkben!')
print('Kérjük, válasszon az alábbi menüpontok közül:')
print()

while True:
    print('------------------------------------------------')
    print('MENÜ')
    print('------------------------------------------------')
    print('''
1. Dolgozók kezelése
2. Autók kezelése
3. Kilépés
''')

    selected_menu_item = input('A választott menüpont (1-3): ')

    if selected_menu_item == '1':
        print('------------------------------------------------')
        print('MENÜ - Dolgozók kezelése')
        print('------------------------------------------------')
        print('''
1. Dolgozók listázása
2. Dolgozó hozzáadása
3. Dolgozó törlése
4. Főmenü
5. Kilépés''')
        print()

        selected_menu_item = input('A választott menüpont (1-5): ')

        if selected_menu_item == '1':
            counter = 1
            for employee in EMPLOYEES:
                print(f'{counter}. {employee[0]}, {employee[1]} years old.')
                counter += 1
        elif selected_menu_item == '2':
            pass
        elif selected_menu_item == '3':
            pass
        elif selected_menu_item == '4':
            pass
        elif selected_menu_item == '5':
            print()
            print('A viszontlátásra!')
            break
        else:
            print('------------------------------------------------')
            print('HIBA: NINCS ILYEN DOLGOZÓ KEZELÉSI MENÜPONT!')
            print('------------------------------------------------')

    elif selected_menu_item == '2':
        print('------------------------------------------------')
        print('MENÜ - Autók kezelése')
        print('------------------------------------------------')
        print('''
1. Autók listázása
2. Autó hozzáadása
3. Autó törlése
4. Főmenü
5. Kilépés''')
        print()

        selected_menu_item = input('A választott menüpont (1-5): ')

        if selected_menu_item == '1':
            counter = 1
            for car in CARS:
                print(f'{counter}. {car[0]} ({car[1]},', end='')
                if car[2]:
                    print('benzin)')
                else:
                    print('diesel)')
                counter += 1
        elif selected_menu_item == '2':
            pass
        elif selected_menu_item == '3':
            pass
        elif selected_menu_item == '4':
            pass
        elif selected_menu_item == '5':
            print()
            print('A viszontlátásra!')
            break
        else:
            print('------------------------------------------------')
            print('HIBA: NINCS ILYEN AUTÓ KEZELÉSI MENÜPONT!')
            print('------------------------------------------------')

    elif selected_menu_item == '3':
        print()
        print('A viszontlátásra!')
        break
    else:
        print('------------------------------------------------')
        print('HIBA: NEM MEGFELELŐ MENÜPONTOT ADOTT MEG!')
        print('------------------------------------------------')

    print() # Minden ciklus végén legyen egy üres sor beszúrva - szépészeti beavatkozás
