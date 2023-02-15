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


# 1. feladat megoldása jöhet ide

print('1. feladat')
print()

exit_string = False
print('Kérlek írj be néhány szót (kilépéshez: exit)')

while not exit_string:
    user_string = input()
    if user_string.lower() == 'exit':
        print("Köszi a játékot! Szia! :)")
        exit_string = True
    else:
        reversed_string = user_string[::-1]
        print(user_string, '--->', reversed_string)
