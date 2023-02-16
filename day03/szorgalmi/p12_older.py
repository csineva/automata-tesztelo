print('************ 12. feladat ******************')
'''
A szkripted számolja és írja ki, hogy hány év múlva lesz egy apa kétszer olyan idős, mint a fia.
Az adatokat a felhasználótól kérd be!
A szkripted kezelje azt is, ha ez a duplázódás a múltban volt.
'''

atya = int((input('Apa életkora: ')))
fiu = int((input('Fia életkora: ')))

evek_szama = 0

if atya % 2 == 0:
    evek_szama = int((atya / 2 - fiu) * 2)
else:
    evek_szama = int((((atya -1) / 2 - fiu) * 2) + 1)

if atya - fiu == fiu:
    print('Az apa épp most kétszer olyan idős, mint a fia')
elif atya - fiu > fiu:
    print(f'{evek_szama} év múlva az apa ({atya + evek_szama}) éppen kétszer annyi idős lesz,')
    print(f'mint a fia ({fiu + evek_szama})')
else:
    print(f'{abs(evek_szama)} éve az apa ({atya - abs(evek_szama)}) éppen kétszer annyi idős volt,')
    print(f'mint a fia ({fiu - abs(evek_szama)})')