print('************ 3. feladat ******************')
'''
Add meg egy felhasználótól bekért szó páratlan helyen lévő betűjeit és írasd őket ki! (pl. alma esetén a megoldás a,m)
'''

inputstr = (input('Kérlek adj meg egy szót: '))
odds = ""

for i in range(len(inputstr)):
    if i % 2 == 0:
        odds += inputstr[i]
    else:
        continue


print("A szó páratlan karakterei: ", odds)