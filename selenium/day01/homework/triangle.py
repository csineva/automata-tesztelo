'''
Feladat: Ellenőrizzük le, megfelelően történik-e a háromszög fajták meghatározása!
Használjunk elágazást és írjunk ki a képernyőre egy az eredménynek megfelelő szöveget!

https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
s = Service(executable_path='e:\selenium\chromedriver.exe')
o = Options()
o.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=s, options=o)
browser.get('https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html')


def check_triangle(a, b, c):
    if a + b <= c or a + c <= b and b + c <= a:
        return 'Error: Not a Triangle'
    elif a == b and b == c:
        return 'Equilateral'
    elif a == b or a == c or b == c:
        return 'Isosceles'
    else:
        return 'Scalene'


def fill_form(a, b, c):
    browser.find_element(By.ID, 'side1').send_keys(a)
    browser.find_element(By.ID, 'side2').send_keys(b)
    browser.find_element(By.ID, 'side3').send_keys(c)
    browser.find_element(By.ID, 'identify-triangle-action').click()
    return browser.find_element(By.ID, 'triangle-type').text


triangles = [
    [10, 10, 10, 'Egyenlő szárú háromszög (Equilateral)'],
    [10, 10, 5, 'Egyenlő oldalú háromszög (Isosceles)'],
    [10, 11, 12, '"Egyenlőtlen" oldalú háromszög (Scalene)'],
    [10, 10, 20, 'Nem háromszög (Not a Triangle)'],
    ]


for i in range(len(triangles)):
    x, y, z, typ = triangles[i]

    filled = fill_form(x, y, z)
    checked = check_triangle(x, y, z)
    print(f'Tesztelt háromszög oldalainak hossza: {x}, {y}, {z}\n'
          f'Elvárt eredmény: {typ}\n'
          f'Kliens oldalon számított eredmény: {checked}\n'
          f'Böngészőben visszakapott érték: {filled}'
          )
    print('_' * 20)
    time.sleep(3)
    if checked == filled:
        print('test PASSED')
        print()
    else:
        print('test FAILED')
        print()

    browser.refresh()

browser.close()

