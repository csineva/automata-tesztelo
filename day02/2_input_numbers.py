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

numbers = []
alma = []
nr_of_numbers = int(input('Hány számot szeretnél megadni?'))
print(f'Kérlek írd be egyenként ezt az {nr_of_numbers} számot:')

for number in range(nr_of_numbers):
    numbers.append(int(input(f'{number + 1}. szám: ')))

print(f'A következő számokat adtad meg: {numbers}')
print(f'Minden második szám: {numbers[1::2]}')
numbers.sort(reverse=True)
print(f'A számaid csökkenő sorrendben: {sorted(numbers, reverse=True)}')

# str.sort() sorba rendezést miért nem lehet változóba menteni?