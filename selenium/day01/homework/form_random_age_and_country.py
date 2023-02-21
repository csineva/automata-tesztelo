'''
Feladat: Töltsük ki a form-ot python kód segítségével!
Szorgalmi: Próbáljuk meg beküldeni az adatokat!

https://testpages.herokuapp.com/styled/validation/input-validation.html
'''
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


s = Service(executable_path='c:\selenium\chromedriver.exe')
o = Options()
o.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=s, options=o)
browser.get('https://testpages.herokuapp.com/styled/validation/input-validation.html')

title = browser.current_url

firstname = browser.find_element(By.ID, 'firstname')
surname = browser.find_element(By.ID, 'surname')
age = browser.find_element(By.ID, 'age')
notes = browser.find_element(By.ID, 'notes')
submit_button = browser.find_element(By.CSS_SELECTOR, 'body > div > div:nth-child(7) > '
                                                      'form > input[type=submit]:nth-child(31)')  # css 2. OK



# randomly selected country fun--------------------------------------------------
country = browser.find_elements(By.TAG_NAME, 'option')
print(f'A listában {len(country)} ország található.')
print()
random_country = random.randint(0, len(country))
selected_country = browser.find_element(By.XPATH, f'//*[@id="country"]/option[{random_country}]')
selected_country_text = selected_country.text
print(f'Random ország kiválasztása: {selected_country.text}')
selected_country.click()
# ---------------------------------------------------------------------------------


firstname.send_keys('some firstname')
surname.send_keys('some surname')
age.send_keys(str(random.randint(18, 65)))
notes.send_keys('some notes goes here')
time.sleep(4)
submit_button.click()

# submit testing
title_sent = browser.current_url
submitted_country = browser.find_element(By.ID, 'country-value')


if selected_country_text == submitted_country.text:
    print(f'{submitted_country.text} rögzítése sikerült.')

if title_sent == title:
    print('Űrlap elküldése sikertelen')
else:
    print('Az űrlap elküldve!')


# country = browser.find_element(By.ID, 'country')                                         #  useless here
# country = browser.find_element(By.CSS_SELECTOR, '#country > option:nth-child(38)')       #  css 1. FAIL
# country = browser.find_element(By.CSS_SELECTOR, 'css=input:nth-child(31)')               #  css 2. FAIL
# country = browser.find_element(By.XPATH, '//*[@id="country"]/option[76]')                #  xpath 1. OK
# country = browser.find_element(By.XPATH, '//*[@id="country"]/option[text()="Honduras"]') #  xpath 2. OK

# submit_button = browser.find_element(By.XPATH, '/html/body/div/div[3]/form/input[4]') #  xpath 1. OK
# submit_button = browser.find_element(By.XPATH, '//input[@type="submit"]')             #  xpath 2. OK
# submit_button = browser.find_element(By.XPATH, '//input[4]')                          #  xpath 3. OK
# submit_button = browser.find_element(By.CSS_SELECTOR, 'input:nth-child(31)')          #  css 1. OK