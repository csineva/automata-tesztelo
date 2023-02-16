print('************ 2. feladat ******************')
'''
Kérj be a felhasználótól három számot!
Add meg a három szám összegét, kivéve ha a három szám azonos, akkor a szorzatukat add meg!
'''

nums = []

print("kérlek adj meg három számot!")
for i in range(3):
    nums.append(int(input(f'{i + 1}. szám: ')))

if nums.count(nums[0]) == 3:
    prod = 1
    for i in range(len(nums)):
        prod = prod * nums[i]
    print('A három szám egyenlő. A szorzatuk: ', prod)
else:
    sum = sum(nums)
    print('A három szám összege', sum)

