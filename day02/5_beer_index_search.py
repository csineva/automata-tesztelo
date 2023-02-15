"""---------------------------------------------------------------------------------------------------------------------
SZORGALMI
A megadott stringben keressük meg az összes 'sör' előfordulást és tároljuk el az indexüket egy listában
"""
import time

sentence = 'Egy sör nem sör. 2 sör fél sör. 4 sör 1 sör. 1 sör meg nem sör...'
sorindexek = []
vege = False
pointer = 0

print("Sörkeresés indul az alábbi mintában:")
for i in sentence:
    print(i, end='')
    time.sleep(.02)

print()
print('-' * len(sentence))
time.sleep(2)

while not vege:
    pointer = sentence.find('sör', pointer)
    if pointer > -1:
        sorindexek.append(pointer)
        print(f'Hoppá! Nicsak, itt is egy sör: [{pointer}]')
        pointer += 1

        time.sleep(.3)
    else:
        vege = True
print()
print('*' * len(sentence))
print('Sörökkévalóság!', sorindexek)
print('*' * len(sentence))
