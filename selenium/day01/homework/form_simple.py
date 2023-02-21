'''
Feladat: Töltsük ki a form-ot python kód segítségével!
Szorgalmi: Próbáljuk meg beküldeni az adatokat!

https://testpages.herokuapp.com/styled/validation/input-validation.html
'''

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
country = browser.find_element(By.XPATH, '//*[@id="country"]/option[text()="Hungary"]')
notes = browser.find_element(By.ID, 'notes')
submit_button = browser.find_element(By.XPATH, '//input[@type="submit"]')
country.click()

firstname.send_keys('some firstname')
surname.send_keys('some surname')
age.send_keys('32')
notes.send_keys('some notes goes here')
submit_button.click()

# submit testing
title_sent = browser.current_url

if title_sent == title:
    print('Űrlap elküldése sikertelen')
else:
    print('Az űrlap elküldve!')
