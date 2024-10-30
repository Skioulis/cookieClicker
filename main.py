from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import timeLoop
import timeLoop as tL
import time

def can_buy (item):
    if item.get_attribute("class") == "":
        print("can buy")
        return True
    print("can't buy")
    return False

def initialization ():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")

    inner_driver = webdriver.Chrome(options=chrome_options)
    inner_driver.get("https://orteil.dashnet.org/experiments/cookie/")
    return inner_driver

def cookie_shop(inner_driver : webdriver):

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
        "time_machine": time_machine,
        "portal": portal,
        "alchemy_lab": alchemy_lab,
        "shipment": shipment,
        "mine": mine,
        "factory": factory,
        "grandma": grandma,
        "cursor":cursor,
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
        "money" : string_to_int(money),
        "cursor" : string_to_int(cursor_price),
        "grandma" : string_to_int(grandma_price),
        "factory" : string_to_int(factory_price),
        "mine" : string_to_int(mine_price),
        "shipment" : string_to_int(shipment_price),
        "alchemy_lab" : string_to_int(alchemy_lab_price),
        "portal" : string_to_int(portal_price),
        "time_machine" : string_to_int(time_machine_price)
    }

def string_to_int (string : str):

    if ',' in string:

        string = string.replace(',','')

    return int(string)

driver = initialization()

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')




def buy_from_shop():
    # found the grayed class will try with this
    while True:
        shop = cookie_shop(driver)
        prices = get_prices(driver)
        print(prices['grandma'])
        # the ifs are working
        if prices["money"] > prices["time_machine"]:
            print(f"buying timemachine @ {prices["time_machine"]}")
            shop["time_machine"].click()

        elif prices["money"] > prices["portal"]:
            print(f"buying portal @ {prices["portal"]}")
            shop["portal"].click()

        elif prices["money"] > prices["alchemy_lab"]:
            print(f"buying alchemy_lab @ {prices["alchemy_lab"]}")
            shop["alchemy_lab"].click()

        elif prices["money"] > prices["shipment"]:
            print(f"buying shipment @ {prices["shipment"]}")
            shop["shipment"].click()

        elif prices["money"] > prices["mine"]:
            print(f"buying mine @ {prices["mine"]}")
            shop["mine"].click()

        elif prices["money"] > prices["factory"]:
            print(f"buying factory @ {prices["factory"]}")
            shop["factory"].click()

        elif prices["money"] > prices["grandma"]:
            print(f"buying grandma @ {prices["grandma"]}")
            shop["grandma"].click()

        elif prices["money"] > prices["cursor"]:
            print(f"buying cursor @ {prices["cursor"]}")
            shop["cursor"].click()
        else:
            break

    print("done buying")

tL.run_for_five_sec(cookie)

# shop = cookie_shop(driver)
money = string_to_int(driver.find_element(By.ID, value="money").text)
grandma = driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]')
# grandma.get_attribute()
has_money = True
shop = cookie_shop(driver)

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)


# while has_money:
#
#
#
#     for key, value in shop.items():
#         if can_buy(value):
#             value.click()
#
#         else:
#             has_money = False










# driver.quit()
