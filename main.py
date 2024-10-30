from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import timeLoop
import timeLoop as tL
import time



def initialization ():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://orteil.dashnet.org/experiments/cookie/")
    return driver

def cookie_shop(inner_driver : webdriver):

    cookie = inner_driver.find_element(By.XPATH, value='//*[@id="cookie"]')
    cursor = inner_driver.find_element(By.XPATH, value='//*[@id="buyCursor"]')
    grandma = inner_driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]')
    factory = inner_driver.find_element(By.XPATH, value='//*[@id="buyFactory"]')
    mine = inner_driver.find_element(By.XPATH, value='//*[@id="buyMine"]')
    shipment = inner_driver.find_element(By.XPATH, value='//*[@id="buyShipment"]')
    alchemy_lab = inner_driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]')
    portal = inner_driver.find_element(By.XPATH, value='//*[@id="buyPortal"]')
    time_machine = inner_driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]')

    print("shop done") # delete

    return {
        "cookie": cookie,
        "cursor":cursor,
        "grandma":grandma,
        "factory":factory,
        "mine":mine,
        "shipment":shipment,
        "alchemy_lab":alchemy_lab,
        "portal":portal,
        "time_machine":time_machine,
    }

def get_prices(inner_driver : webdriver):
    money = inner_driver.find_element(By.ID, value="money").text
    cursor_price = inner_driver.find_element(By.XPATH, value='//*[@id="buyCursor"]/b').text.split(' - ')[1]
    grandma_price =  inner_driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]/b').text.split(' - ')[1]
    factory_price =  inner_driver.find_element(By.XPATH, value='//*[@id="buyFactory"]/b').text.split(' - ')[1]
    mine_price = inner_driver.find_element(By.XPATH, value='//*[@id="buyMine"]/b').text.split(' - ')[1]
    shipment_price = inner_driver.find_element(By.XPATH, value='//*[@id="buyShipment"]/b').text.split(' - ')[1]
    alchemy_lab_price = inner_driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b').text.split(' - ')[1]
    portal_price = inner_driver.find_element(By.XPATH, value='//*[@id="buyPortal"]/b').text.split(' - ')[1]
    time_machine_price = inner_driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b').text.split(' - ')[1]

    print("prices done")

    return {
        "money" : money,
        "cursor_price" : cursor_price,
        "grandma_price" : grandma_price,
        "factory_price" : factory_price,
        "mine_price" : mine_price,
        "shipment_price" : shipment_price,
        "alchemy_lab_price" : alchemy_lab_price,
        "portal_price" : portal_price,
        "time_machine_price" : time_machine_price
    }

driver = initialization()

shop = cookie_shop(driver)
prices = get_prices(driver)


# def cookie_loop(element):
#     tL.run_for_five_sec(element['cookie'])





        # return {
        #     "money" : money.text ,
        #     "cursor_price_int":cursor_price_int}

    # prices = check_price()
    # print(prices["money"])
    # while int(prices['money'].text) > prices['cursor_price_int']:
    #     element['cursor'].click()


shop = cookie_shop(driver)







# cookie_loop(elements)

# print(int(cursor_price.text.replace('Cursor - ', '')))
