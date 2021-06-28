from logopas import login, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, random

browser = None

def login_chrome_firefox(_browser, login, password):
    global browser
    if _browser == 'Chrome':
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com')
    time.sleep(random.randrange(2,7))

    _login = browser.find_element(By.NAME,'username')
    _login.clear()
    _login.send_keys(login)

    time.sleep(random.randrange(2, 3))

    _password = browser.find_element(By.NAME, 'password')
    _password.clear()
    _password.send_keys(password)

    time.sleep(random.randrange(2, 3))

    _login_button = browser.find_element_by_css_selector('button[type="submit"]')
    _login_button.click()


def close_browser():
    global browser
    browser.close()
    browser.quit()

def search_by_hashtag(hashtag):
    global browser
    browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")

    for i in range(1,4):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(random.randrange(2,5))

    hrefs = browser.find_elements_by_tag_name('a')
    urls = [item.get_attribute('href') for item in hrefs  if "/p/" in item.get_attribute('href')]
    print(urls)

    for url in urls:
        browser.get(url)
        time.sleep(random.randrange(3, 5))
        like = browser.find_element(By.XPATH,"/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
        like.click()
        time.sleep(random.randrange(85, 105))


login_chrome_firefox('Chrome', login, password)
time.sleep(5)
search_by_hashtag("kazan")
time.sleep(100)
close_browser()