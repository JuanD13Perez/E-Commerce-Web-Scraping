from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time

df = pd.read_excel('Products_and_comp.xlsx')
productos = df['Material']
competencia = df.columns[3::2]

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.mercadolibre.com.mx/")

try:
    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "nav-search-input"))
    )
    search_bar.clear()
    search_bar.send_keys(productos[0])
    search_bar.send_keys(Keys.RETURN)

    try:
        xpath1 = "//h2[@class='ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title']"
        xpath2 = "//h2[@class='ui-search-item__title shops__item-title']"
        title_products = driver.find_elements(By.XPATH, xpath2)
        title_products = [title.text for title in title_products]
        

        xpathp = "//div[@class='ui-search-price ui-search-price--size-medium shops__price']//span[@class='price-tag-fraction']"
        price_products = driver.find_elements(By.XPATH,xpathp)
        price_products = [price.text for price in price_products]

        xpathl = "//div[@class='ui-search-item__group ui-search-item__group--title shops__items-group']//a[1]"
        links = driver.find_elements(By.XPATH, xpathl)
        links = [link.get_attribute("href") for link in links]
        
    except:
        print('It was not possible to get titles, prices and links')

    products = {
        'titles': title_products,
        'prices': price_products,
        'links': links
    }

    df = pd.DataFrame(products)
    df['id'] = productos[0]
    df.to_csv('test_ML.csv')
finally:
    driver.quit()
