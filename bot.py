from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('headless')
PATH = '/usr/local/share/chromedriver'
driver = webdriver.Chrome(PATH, options=option) # Selenium also supports edge and firefox
driver.get("https://kontakt.az/?s=iphone+11")

print(driver.title)
driver.quit()


