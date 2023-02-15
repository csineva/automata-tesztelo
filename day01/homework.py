"""
1. Feladat
Kérj be a felhasználótól 2 db számot és írasd ki a következő képletek eredményét
-  (a + b) * (a - b)
-  (a hatvány b) - (a és b szorzata)
-  a / b maradéka és egész értéke
"""

print()
print('1. feladat megoldása:')
print()

a = int(input('Kérlek adj meg két egész számot!\nElső szám (a): '))
b = int(input('Második szám (b): '))
mod = a % b

print('(a + b) * (a - b) = ' + str((a + b) * (a - b)))
print('(a hatvány b) - (a és b szorzata) =', (a ** b) - (a * b))
print(f'a / b maradéka = {mod}')
print(f'a / b egész értéke = {a // b}')


"""---------------------------------------------------------------------------------------------------------------------
2. feladat
Az alábbi változó tartalmaz 3 gyümölcsöt.
Slice-olással mentsd ki a gyümölcsöket külön változókba,
majd végezz el rajtuk műveleteket úgy, hogy a következő kimenetet kapd:

OUTPUT:
APPLE (hossz: 5)
orange (hossz: 6)
ananab (hossz: 6)

"""
print()
print('2. feladat megoldása:')
print()

fruits = 'apple OrAnGe banana'

alma = fruits[:5].upper()
narancs = fruits[6:12].lower()
banan = fruits[-6:][::-1]

print(alma + ' (hossz: ' + str(len(alma)) + ')')
print(f'{narancs} (hossz: {len(narancs)})')
print(banan, ' (hossz: ', len(banan), ')', sep='')

# 2.
print(f'''
{alma} (hossz: {len(alma)})
{narancs} (hossz: {len(narancs)})
{banan} (hossz: {len(banan)})
''')

"""---------------------------------------------------------------------------------------------------------------------
3. feladat
Az alábbi változó tartalmaz egy rejtjelezett szöveget.
Ha csak minden 3. karaktert olvasol össze, akkor kapod meg az eredeti, értelmes üzenetet.
Írasd ki a képernyőre a megfejtést!
"""
print()
print('3. feladat megoldása:')
print()

secret_message = 'QmRgFeusjbetUlőGKzkCkSYöxKdMXőuK GsPYiywTtBehewoNIn'

decrypded_message = secret_message[2::3]
print(decrypded_message)


"""---------------------------------------------------------------------------------------------------------------------
4. feladat
Menüpont választás. Írasd ki a képernyőre az alábbi szöveget:

Üdvözöllek!
1. Kirándulás
2. TV nézés
3. Tanulás

Kérj be a felhasználótól egy menüpontot (1-3) és a választásnak megfelelően írj ki egy szöveget a képernyőre.
"""

print()
print('4. feladat megoldása:')
print()

kirandulas = 'Ma ki fogunk rándulni! :)'
tv_nezes = 'Ma végignézzük a "Borgen" harmadik évadát!'
tanulas = 'Ma bizony stringeket fogunk szeletelni...'

print('''Üdvözöllek!
1. Kirándulás
2. TV nézés
3. Tanulás''')

tevekenyseg = int(input('Kérlek válassz a fenti tevékenységek közül (1-3): '))

if tevekenyseg == 1:
    print(kirandulas)
elif tevekenyseg == 2:
    print(tv_nezes)
elif tevekenyseg == 3:
    print(tanulas)
else:
    print("Ilyen tevékenység a világon nincs!")
