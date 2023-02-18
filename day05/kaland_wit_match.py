data = [
    'Te vagy az iskola rosszfiúja. Késve érkezel a suli elé, még elszívod a cigidet, aztán…',
    'Észreveszi az éppen érkező töri tanárod, mit tettél és…',
    '2. elnyomod a csikket az igazgatónő bringájának kerekébe.',
    '3. felrúgod a bejárat melletti szemeteskukát és mellé pöccinted a csikket. ',
    '4. odaér a haverod, Béci is. Rágyújtotok egy újabb cigire. ',
    '5. azonnal felrángat az igazgatói irodába. Te hőzöngve tiltakozol végig a folyosón.',
    '6. gratulál neked, hisz szerinte is egy nagyképű szipirtyó a nő. ',
    '7. szó nélkül tovább sétál, mivel eléggé parázik tőled.',
    '8. az akciód nem jól sül el, mivel az égő csikktől meggyullad a szemét és lángra kap az egész bejárati ajtó.',
    '9. a gondnok meghunyászkodva elkezdi összeseperni a szemetet.',
    '10. pechedre akkor ér oda melléd az a dögös csaj az évfolyamról, akinek szemlátomást nem jön be a viselkedésed.',
    '11. Béci rávesz, hogy lógjátok el az egész napot. Belemész.',
    '12. kiszúrod az éppen közeledő dögös csajt az évfolyamról és megszólítod.',
    '13. kiszúrod az éppen közeledő dögös csajt az évfolyamról és Béci megszólítja.',
    '14. kihúzod magad a tanár kezei közül és röhögve elfutsz előle a folyosón.',
    '15. megbököd a vállát és megkínálod cigivel, elfogadja és rágyújt.',
    '16. Bemész a suliba. Feszkós vagy, ezért betörsz egy ablakot a folyosón.',
    '17. eltűnsz a helyszínről, mintha semmi közöd se lenne a történtekhez.',
    '18. elégedetten szemléled a művedet.',
    '19. a legközelebbi kocsmáig meg se állsz és piszkosul berúgsz.',
    '20. sikerül valami nyálas dumát nyomnod a kék szemeiről. ',
    '21. elküld a francba.',
    '22. a nap hátralévő részében disznó vicceken röhögtök.'
]

choice = 1
exit_game = False


def print_and_choose(*args):
    print()
    for i in args:
        print(data[i])
    print()
    select = int(input('Mit választasz? Írj be a számot: '))
    return select


while not exit_game:
    match choice:
        case 1:
            choice = print_and_choose(0, 2, 3, 4)

        case 2:
            choice = print_and_choose(1, 5, 6, 7)

        case 3:
            choice = print_and_choose(8, 9, 10)

        case 4:
            choice = print_and_choose(11, 12, 13)

        case 5:
            choice = print_and_choose(10, 12, 14)

        case 6:
            choice = print_and_choose(4, 15, 16)

        case 7:
            choice = print_and_choose(12, 15, 16)

        case 8:
            choice = print_and_choose(4, 17, 18)

        case 9:
            choice = print_and_choose(15, 16, 4)

        case 10:
            choice = print_and_choose(15, 7, 17)

        case 11:
            choice = print_and_choose(19, 3, 2)

        case 12:
            choice = print_and_choose(15, 20, 21)

        case 13:
            choice = print_and_choose(16, 3, 2)

        case 14:
            choice = print_and_choose(19, 21, 12)

        case 15:
            choice = print_and_choose(22)

        case 16:
            choice = print_and_choose(18, 17, 12)

        case 17:
            choice = print_and_choose(19)

        case 18:
            choice = print_and_choose(4)

        case 19:
            print("VÉGE")
            exit_game = True

        case 20:
            choice = print_and_choose(22)

        case 21:
            choice = print_and_choose(19)

        case 22:
            print('VÉGE')
            exit_game = True
