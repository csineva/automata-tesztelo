i = 1

while i != 19 and i != 22:
    if i == 1:
        print('''Te vagy az iskola rosszfiúja. Késve érkezel a suli elé, még elszívod a cigidet, aztán…
2. elnyomod a csikket az igazgatónő bringájának kerekébe.
3. felrúgod a bejárat melletti szemeteskukát és mellé pöccinted a csikket. 
4. odaér a haverod, Béci is. Rágyújtotok egy újabb cigire. 
''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 2 or v == 3 or v == 4:
            i = v

    if i == 2:
        print('''észreveszi az éppen érkező töri tanárod, mit tettél és…
5. azonnal felrángat az igazgatói irodába. Te hőzöngve tiltakozol végig a folyosón.
6. gratulál neked, hisz szerinte is egy nagyképű szipirtyó a nő. 
7. szó nélkül tovább sétál, mivel eléggé parázik tőled.
''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 5 or v == 6 or v == 7:
            i = v

    if i == 3:
        print('''8. az akciód nem jól sül el, mivel az égő csikktől meggyullad a szemét és lángra kap az egész bejárati ajtó.
    9. a gondnok meghunyászkodva elkezdi összeseperni a szemetet.
    10. pechedre akkor ér oda melléd az a dögös csaj az évfolyamról, akinek szemlátomást nem jön be a viselkedésed.
    ''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 8 or v == 9 or v == 10:
            i = v

    if i == 4:
        print('''11. Béci rávesz, hogy lógjátok el az egész napot. Belemész.
12. kiszúrod az éppen közeledő dögös csajt az évfolyamról és megszólítod.
13. kiszúrod az éppen közeledő dögös csajt az évfolyamról és Béci megszólítja.
''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 11 or v == 12 or v == 13:
            i = v

    if i == 5:
        print('''10. pechedre akkor ér oda melléd az a dögös csaj az évfolyamról, akinek szemlátomást nem jön be a viselkedésed.
12. kiszúrod az éppen közeledő dögös csajt az évfolyamról és megszólítod.
14. kihúzod magad a tanár kezei közül és röhögve elfutsz előle a folyosón.
''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 10 or v == 12 or v == 14:
            i = v

    if i == 6:
        print('''4. odaér a haverod, Béci is. Rágyújtotok egy újabb cigire.
15. megbököd a vállát és megkínálod cigivel, elfogadja és rágyújt.
16. Bemész a suliba. Feszkós vagy, ezért betörsz egy ablakot a folyosón.
                ''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 4 or v == 15 or v == 16:
            i = v


    if i == 7:
        print('''szó nélkül tovább sétál, mivel eléggé parázik tőled. Ezért...
12. kiszúrod az éppen közeledő dögös csajt az évfolyamról és megszólítod.
15. megbököd a vállát és megkínálod cigivel, elfogadja és rágyújt.
16. Bemész a suliba. Feszkós vagy, ezért betörsz egy ablakot a folyosón.
    ''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 12 or v == 15 or v == 16:
            i = v

    if i == 8:
        print('''4. odaér a haverod, Béci is. Rágyújtotok egy újabb cigire.
17. eltűnsz a helyszínről, mintha semmi közöd se lenne a történtekhez.
18. elégedetten szemléled a művedet.

    ''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 4 or v == 17 or v == 18:
            i = v

    if i == 9:
        print('''15. megbököd a vállát és megkínálod cigivel, elfogadja és rágyújt.
16. Bemész a suliba. Feszkós vagy, ezért betörsz egy ablakot a folyosón.
4. odaér a haverod, Béci is. Rágyújtotok egy újabb cigire.
''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 15 or v == 16 or v == 4:
            i = v

    if i == 10:
        print('''
15. megbököd a vállát és megkínálod cigivel, elfogadja és rágyújt.
7. szó nélkül tovább sétál, mivel eléggé parázik tőled.
17. eltűnsz a helyszínről, mintha semmi közöd se lenne a történtekhez.
''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 15 or v == 7 or v == 17:
            i = v

    if i == 11:
        print('''19. a legközelebbi kocsmáig meg se állsz és piszkosul berúgsz.
3. felrúgod a bejárat melletti szemeteskukát és mellé pöccinted a csikket. 
2. elnyomod a csikket az igazgatónő bringájának kerekébe.
''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 19 or v == 3 or v == 2:
            i = v

    if i == 12:
        print('''15. megbököd a vállát és megkínálod cigivel, elfogadja és rágyújt.
20. sikerül valami nyálas dumát nyomnod a kék szemeiről. 
21. elküld a francba.
    ''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 15 or v == 20 or v == 21:
            i = v

    if i == 13:
        print('''16. Bemész a suliba. Feszkós vagy, ezért betörsz egy ablakot a folyosón.
3. felrúgod a bejárat melletti szemeteskukát és mellé pöccinted a csikket. 
2. elnyomod a csikket az igazgatónő bringájának kerekébe.
        ''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 16 or v == 17 or v == 18:
            i = v

    if i == 14:
        print('''kihúzod magad a tanár kezei közül és röhögve elfutsz előle a folyosón. Ezért...
19. a legközelebbi kocsmáig meg se állsz és piszkosul berúgsz.
21. elküld a francba.
12. kiszúrod az éppen közeledő dögös csajt az évfolyamról és megszólítod.

''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 19 or v == 21 or v == 12:
            i = v

    if i == 15:
        print('22. a nap hátralévő részében disznó vicceken röhögtök.')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 22:
            i = v

    if i == 16:
        print('''18. elégedetten szemléled a művedet.
17. eltűnsz a helyszínről, mintha semmi közöd se lenne a történtekhez.
12. kiszúrod az éppen közeledő dögös csajt az évfolyamról és megszólítod.
''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 18 or v == 17 or v == 12:
            i = v

    if i == 17:
        print('''19. a legközelebbi kocsmáig meg se állsz és piszkosul berúgsz.''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 19:
            i = v

    if i == 18:
        print('''4. odaér a haverod, Béci is. Rágyújtotok egy újabb cigire.''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 4:
            i = v

    if i == 20:
        print('''22. a nap hátralévő részében disznó vicceken röhögtök.''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 22:
            i = v

    if i == 21:
        print('''19. a legközelebbi kocsmáig meg se állsz és piszkosul berúgsz.''')
        v = int(input('Mit választasz? Írj be a számot: '))
        if v == 19:
            i == v

    if i == 19 or i == 22:
        print('VÉGE A SZTORINAK')
