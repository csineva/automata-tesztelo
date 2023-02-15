"""---------------------------------------------------------------------------------------------------------------------
3. feladat
Kérjünk be neveket a felhasználótól és tároljuk őket egy listában.
Minden név felvétel után kérdezzük meg, hogy akar-e még nevet felvenni.
Ha igen --> ismételjük az előzőeket
Ha nem --> kérdezzük meg, hogy csökkenő vagy növekvő sorrendben szeretné-e látni a névsort.
Írassuk ki a névsort a kért módon.
"""

# 3. feladat megoldása jöhet ide

namelist = []
exitstring = False

print("Kérlek adj meg egy nevet: ")
while not exitstring:
    namelist.append(input())
    more_name = input('Szeretnél még neveket felvenni? (igen: y, nem: bármely más billentyű)')
    if more_name == 'y':
        print("Kérlek adj meg még egy nevet!")
    else:
        exitstring = True
print()
order = input('Növekvő (n) vagy csökkenő (bármely más billentyű) sorrendbe rendezzem a neveket?')
print()
if order == 'n':
    print("A nevek növekvő sorrendben: \n", sorted(namelist))
else:
    print("A nevek Csökkenő sorrendben: \n", sorted(namelist, reverse=True))
