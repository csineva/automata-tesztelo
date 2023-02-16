from anyascii import anyascii

print('************ 11. feladat ******************')
'''
I. Készíts egy szkriptet, ami kijelzi, hogy a felhasználótól bekért szó palindróma-e?
II. Készíts egy szkriptet, ami kijelzi, hogy a felhasználótól bekért mondat palindróma-e?
Palindróma az, ami visszafele olvasva is ugyanazt adja, mint az eredeti. Pl. szó esetén: kék, mondat esetén: Indul a görög aludni.
'''

userstr = input('Kérlek adj meg egy szót vagy mondatot!')

kifilezett = anyascii(userstr.replace(' ', '').replace('.', '').lower())
print(kifilezett)

if kifilezett == kifilezett[::-1]:
    print('A string palindrom!')
else:
    print('Nem palindrom :(')