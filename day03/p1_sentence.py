print('************ 1. feladat ******************')
'''
Adottak a következő szavak: két, macska, van.
Jelenítsd meg őket egy mondatban! (Két macska van.)
Jelenítsd meg őket egy mondatban, de számot használj! (2 monitor van.)
'''

strlist = [2, 'macska', 'van']

for i in range(len(strlist)):
    if type(strlist[i]) != 'str':
        strlist[i] = str(strlist[i])

sentence = " ".join(strlist).capitalize()
print(sentence, '.', sep='')
