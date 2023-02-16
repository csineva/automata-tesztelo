# AUTÓ SZALON - FEJLESZTETT
# Példa kód a függvényesítéshez, modularizálás témakörhöz

from salon import *

# PROGRAM---------------------------------------------------------------------------------------------------------------

print('Üdvözüljük kereskedés menedzsment eszközünkben!')
print('Kérjük, válasszon az alábbi menüpontok közül:')
print()

while True:
    banner('MENÜ')

    selected_menu_item = select_from_menu_main()

    if selected_menu_item == '1':
        banner('MENÜ - Dolgozók kezelése')
        selected_menu_item = select_from_menu_employee()
        print()

        if selected_menu_item == '1':
            list_employee()
        elif selected_menu_item == '2':
            add_employee()
        elif selected_menu_item == '3':
            remove_empoyee()
        elif selected_menu_item == '4':
            continue
        elif selected_menu_item == '5':
            print()
            print('A viszontlátásra!')
            break
        else:
            banner('HIBA: NINCS ILYEN DOLGOZÓ KEZELÉSI MENÜPONT!', border_char='!')

    elif selected_menu_item == '2':
        banner('MENÜ - Autók kezelése')
        selected_menu_item = select_from_menu_car()
        print()

        if selected_menu_item == '1':
            list_cars()
        elif selected_menu_item == '2':
            add_car()
        elif selected_menu_item == '3':
            remove_car()
        elif selected_menu_item == '4':
            continue
        elif selected_menu_item == '5':
            print()
            print('A viszontlátásra!')
            break
        else:
            banner('HIBA: NINCS ILYEN AUTÓ KEZELÉSI MENÜPONT!', border_char='!')

    elif selected_menu_item == '3':
        print()
        print('A viszontlátásra!')
        break
    else:
        banner('HIBA: NEM MEGFELELŐ MENÜPONTOT ADOTT MEG!', border_char='!')

    print() # Minden ciklus végén legyen egy üres sor beszúrva - szépészeti beavatkozás
