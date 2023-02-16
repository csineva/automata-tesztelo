# SETTINGS, DATA--------------------------------------------------------------------------------------------------------

EMPLOYEES = [
    ['Thomas', 42],  # Név, életkor
    ['Jenny', 27]
]

CARS = [
    ['Ford Focus', 2007, True],  # Név, gyártási év, benzines-e
    ['Kia Rio', 2014, False],
    ['Skoda Octavia', 2011, False],
    ['Pözsi 206', 2001, True]
]


# FUNCTIONS --------------------------------------------------------------------------------------------------------


def add_employee():
    employee_data = [input('Kérjük adja meg a dolgozó nevét!'),
                     input('Kérjük adja meg a dolgozó életkorát!')]
    EMPLOYEES.append(employee_data)
    print('A dolgozót rendszerünkben sikeresen rögzítettük!')


def remove_empoyee():
    list_employee()
    selected_employee = int(input(f'Melyik rekordot szeretné törölni? (1-{len(EMPLOYEES)})'))
    print(selected_employee)
    are_you_sure = (input(f'Biztosan ki szeretnéd törölni szegény '
                          f'{EMPLOYEES[selected_employee - 1][0]}-t?(igen/nem)'))
    if are_you_sure.lower() == 'igen':
        are_you_sure2 = (input(f'Lehet hogy van családja, gyermekei... '
                               f'Töröljük ki tényleg? :(( (igen/nem)'))
        if are_you_sure2.lower() == 'igen':
            removed_employee = EMPLOYEES.pop(selected_employee - 1)
            print(f'Szegény {removed_employee[0]} eltávolítva.')


def add_car():
    car_data = [input('Kérjük adja meg az autó típusát!'),
                input('Kérjük adja meg az autó gyártási évét!')]
    fuel_type = (input('Kérjük adja meg az üzemanyag típusát (benzin/diesel)!'))
    if fuel_type.lower() == 'benzin':
        car_data.append(True)
    else:
        car_data.append(False)
    CARS.append(car_data)
    print('Az autót rendszerünkben sikeresen rögzítettük!')


def remove_car():
    list_cars()
    selected_car = int(input(f'Melyik rekordot szeretné törölni? (1-{len(CARS)})'))
    print(selected_car)
    removed_car = CARS.pop(selected_car - 1)
    print(f'Szegény {removed_car[0]} eltávolítva.')


def banner(message, border_char='-'):
    print(border_char * (len(message) + 4))
    print(f'| {message} |')
    print(border_char * (len(message) + 4))


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
    print(f'A dolgozók listája ({len(EMPLOYEES)} fő):')
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
