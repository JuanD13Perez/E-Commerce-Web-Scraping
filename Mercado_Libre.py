from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import numpy as np
import time

df = pd.read_excel('Products_and_comp.xlsx')
productos = df['Material']
competencia = df.columns[3::2]

datos = []

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.mercadolibre.com.mx/")
for i in range(18):
    try:
        # search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "nav-search-input")))
        search_bar = driver.find_element(By.CLASS_NAME, "nav-search-input")
        search_bar.clear()
        search_bar.send_keys(productos[i])
        search_bar.send_keys(Keys.RETURN)

        try:
            #xpath2 = "//h2[@class='ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title']"
            xpath = "//h2[@class='ui-search-item__title shops__item-title']"
            title_products = driver.find_elements(By.XPATH, xpath)
            title_products = [title.text for title in title_products]
            

            xpathp = "//div[@class='ui-search-price ui-search-price--size-medium shops__price']//span[@class='price-tag ui-search-price__part shops__price-part']//span[@class='price-tag-fraction']"
            price_products = driver.find_elements(By.XPATH,xpathp)
            price_products = [price.text for price in price_products]

            xpathl = "//div[@class='ui-search-item__group ui-search-item__group--title shops__items-group']//a[1]"
            links = driver.find_elements(By.XPATH, xpathl)
            links = [link.get_attribute("href") for link in links]

            if len(links) == 0 or len(price_products) == 0 or len(title_products) == 0:
                xpath2 = "//h2[@class='ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title']"
                #xpath = "//h2[@class='ui-search-item__title shops__item-title']"
                title_products = driver.find_elements(By.XPATH, xpath2)
                title_products = [title.text for title in title_products]
                

                xpathp = "//div[@class='ui-search-price ui-search-price--size-medium shops__price']//span[@class='price-tag ui-search-price__part shops__price-part']//span[@class='price-tag-fraction']"
                price_products = driver.find_elements(By.XPATH,xpathp)
                price_products = [price.text for price in price_products]

                xpathl = "//div[@class='ui-search-result__wrapper shops__result-wrapper']//div[@class = 'ui-search-result__image shops__picturesStyles']//a[1]"
                links = driver.find_elements(By.XPATH, xpathl)
                links = [link.get_attribute("href") for link in links]
                if len(links) == len(price_products) and len(price_products) == len(title_products) and len(title_products):
                    products = {'titles': title_products,  'prices': price_products, 'links': links }
                    df = pd.DataFrame(products)
                    df['id'] = productos[i]
                    datos.append(df)

            elif len(links) == len(price_products) and len(price_products) == len(title_products) and len(title_products):
                products = {'titles': title_products,  'prices': price_products, 'links': links }
                df = pd.DataFrame(products)
                df['id'] = productos[i]
                datos.append(df)
            else:
                df = pd.DataFrame({'titles': [np.nan], 'prices': [np.nan], 'links': [np.nan], 'id': productos[i]})
                print('Product Not Available:' + str(productos[i]) + ' pos ' + str(i))
                datos.append(df)
            
        except:
            df = pd.DataFrame({'titles': [np.nan], 'prices': [np.nan], 'links': [np.nan], 'id': productos[i]})
            print('No link for product:' + str(productos[i] + 'pos ' + str(i)))
            datos.append(df)
    except:
        print('Error in buttom in pos ' + str(i))

driver.quit() 
datos_final = pd.concat(datos, ignore_index = True)
datos_final.to_csv('scrapped_csv/Mercado_Libre.csv')