from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import timeLoop
import timeLoop as tL
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

cursor = driver.find_element(By.XPATH, value='//*[@id="buyCursor"]')
grandma = driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]')
factory = driver.find_element(By.XPATH, value='//*[@id="buyFactory"]')
mine = driver.find_element(By.XPATH, value='//*[@id="buyMine"]')
shipment = driver.find_element(By.XPATH, value='//*[@id="buyShipment"]')
alchemy_lab = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]')
portal = driver.find_element(By.XPATH, value='//*[@id="buyPortal"]')
time_machine = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]')
money = driver.find_element(By.ID, value="money")

cursor_price = driver.find_element(By.XPATH, value='//*[@id="buyCursor"]/b')

cursor_price_int = int(cursor_price.text.replace('Cursor - ', ''))

def cookieLoop():
    tL.run_for_some_time(cookie)
    while int(money.text) > cursor_price_int:
        cursor.click()

cookieLoop()

# print(int(cursor_price.text.replace('Cursor - ', '')))
# print(money.text)
# driver.quit()