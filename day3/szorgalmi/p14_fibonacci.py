print('************ 14. feladat ******************')
'''
Írd ki a Fibonacci sor első tíz elemét!
A sor kezdődjön 0-val és 1-gyel.
(Fibonacci sor: két egymást követő elem összege egyenlő a követő elemmel. 0,1,1,2,3,5,8,...
'''

fibo = [0, 1]

for i in range(8):
    fibo.append(fibo[i] + fibo[i + 1])
print(fibo)