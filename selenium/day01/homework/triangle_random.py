'''
Feladat: Ellenőrizzük le, megfelelően történik-e a háromszög fajták meghatározása!
Használjunk elágazást és írjunk ki a képernyőre egy az eredménynek megfelelő szöveget!

https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html
'''
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(executable_path='c:\selenium\chromedriver.exe')
o = Options()
o.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=s, options=o)
browser.get('https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html')


def check_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
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


def check_result(a, b, c):
    filled = fill_form(a, b, c)
    checked = check_triangle(a, b, c)
    print(f'Oldalak: {a: >3}, {b: >3}, {c: >3} '
          f'Elvárt: {checked: <24} '
          f'Kapott: {filled: <24} ',
          end='')
    if checked == filled:
        print(f'{"PASS": <5}')
    else:
        print(f'{"FAIL": >10}')


triangles = [
    [10, 10, 10],  # Egyenlő szárú háromszög (Equilateral)
    [10, 10, 5],  # Egyenlő oldalú háromszög (Isosceles)
    [10, 11, 12],  # Nem egyenlő oldalú háromszög (Scalene)
    [10, 10, 20],  # Nem háromszög (Not a Triangle)
]

# static data from triangles list
for i in range(len(triangles)):  # for i in triangles nem működik valamiért
    x, y, z = triangles[i]

    check_result(x, y, z)
    browser.refresh()

# random data between 1:100
print()
print('_' * 10, 'Random data: ', '_' * 10)
for i in range(10):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    z = random.randint(1, 100)

    check_result(x, y, z)
    browser.refresh()

browser.close()
