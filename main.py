from logopas import login, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

def login_chrome_firefox(_browser, login, password):
    if _browser == 'Chrome':
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com')
    time.sleep(10)
    browser.close()
    browser.quit()

login_chrome_firefox('Chrome', login, password)