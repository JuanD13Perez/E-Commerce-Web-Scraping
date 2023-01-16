import random

datos = []
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.costco.com.mx/")

search_xpath = "//div[@id='searchBoxContainer']//input[@class='search-input']"
search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
search_bar = driver.find_element(By.XPATH, search_xpath)

condition = True
i = 0
while condition and i < 425:
    tiempo_s = round(1+ random.random()*2,2)
    
    if i % 25 == 0:
        time.sleep(5) # We give the page some more free time to load
        
    try:
        #Here we delete the previous search
        search_bar.send_keys(Keys.CONTROL, 'a')
        search_bar.send_keys(Keys.BACKSPACE)

        #We write our new search
        search_bar.send_keys(productos[i])
        search_bar.send_keys(Keys.ENTER)
        time.sleep(tiempo_s)
        try:
            xpath_noresult= "//h1//span[@class='ng-star-inserted']"
            no_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_noresult)))
            no_result = driver.find_element(By.XPATH, xpath_noresult)
            
            if no_result.text != str("No se encontraron resultados para"):
                condition = False
                valor = producto_actual
            
        except:
            condition = False
            valor = producto_actual
            
        
    except:
        print('Falla en Botón de búsqueda' + str(producto_actual))
    i += 1
    

driver.quit() 