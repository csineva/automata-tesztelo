# SETTINGS, DATA--------------------------------------------------------------------------------------------------------

EMPLOYEES = [
    ['Thomas', 42], # Név, életkor
    ['Jenny', 27]
]

CARS = [
    ['Ford Focus', 2007, True], # Név, gyártási év, benzines-e
    ['Kia Rio', 2014, False]
]

# FUNCTIONS --------------------------------------------------------------------------------------------------------


def banner(message, border_char='-'):
    print(border_char * (len(message)+4))
    print(f'| {message} |')
    print(border_char * (len(message)+4))


def select_from_menu_main():
    print('''
1. Dolgozók kezelése
2. Autók kezelése
3. Kilépés
''')

    return input('A választott menüpont (1-3): ')

def select_from_menu_employee():
    print('''
1. Dolgozók listázása
2. Dolgozó hozzáadása
3. Dolgozó törlése
4. Főmenü
5. Kilépés''')

    return input('A választott menüpont (1-5): ')

def select_from_menu_car():
    print('''
1. Autók listázása
2. Autó hozzáadása
3. Autó törlése
4. Főmenü
5. Kilépés''')

    return input('A választott menüpont (1-5): ')

def list_employee():
    counter = 1
    for employee in EMPLOYEES:
        print(f'{counter}. {employee[0]}, {employee[1]} years old.')
        counter += 1

def list_cars():
    counter = 1
    for car in CARS:
        print(f'{counter}. {car[0]} ({car[1]},', end='')
        if car[2]:
            print('benzin)')
        else:
            print('diesel)')
        counter += 1