import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# initial setup
chrome_driver_path = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
# game url and page loading
game_url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(url=game_url)

# let website load then...
time.sleep(4)
# check for language selection pop-up, then click
lang_selection = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
lang_selection.click()

# wait for page transition then find our cookie
time.sleep(4)
cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")


def play_game():
    # products
    cursor = driver.find_element(By.CSS_SELECTOR, "#product0")
    grandma = driver.find_element(By.CSS_SELECTOR, "#product1")
    warehouse = driver.find_element(By.CSS_SELECTOR, "#product2")
    factory = driver.find_element(By.CSS_SELECTOR, "#product3")

    # product prices
    cursor_price = driver.find_element(By.CSS_SELECTOR, "#productPrice0").text
    grandma_price = driver.find_element(By.CSS_SELECTOR, "#productPrice1").text
    warehouse_price = driver.find_element(By.CSS_SELECTOR, "#productPrice2").text
    factory_price = driver.find_element(By.CSS_SELECTOR, "#productPrice3").text

    timeout = 60
    timeout_start = time.time()
    cookies_per_second = ""

    while time.time() < timeout_start + timeout:
        test = 0
        if test == 5:
            break
        test -= 1

        # score data
        score_data = driver.find_element(By.CSS_SELECTOR, "#cookies.title")
        score_list = score_data.text.split()
        score = score_list[0]
        cookies_per_second = score_list[len(score_list) - 1]

        cookie.click()

        if "," in score:
            score = score.replace(",", "")
        if "," in cursor_price:
            cursor_price = cursor_price.replace(",", "")
        if "," in grandma_price:
            grandma_price = grandma_price.replace(",", "")
        if "," in warehouse_price:
            warehouse_price = warehouse_price.replace(",", "")
        if "," in factory_price:
            factory_price = factory_price.replace(",", "")

        score = int(score)

        try:
            if int(factory_price) >= score:
                factory.click()
            elif int(warehouse_price) >= score:
                warehouse.click()
            elif int(grandma_price) >= score:
                grandma.click()
            elif int(cursor_price) >= score:
                cursor.click()
        except ValueError:
            if int(grandma_price) >= score:
                grandma.click()
            elif int(cursor_price) >= score:
                cursor.click()

    print(f"Cookies/sec: {cookies_per_second}.")
    driver.quit()
    return "Done"


play_game()
