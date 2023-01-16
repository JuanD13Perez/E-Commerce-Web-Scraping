datos = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.sears.com.mx/")

no_encontrados = []

for i in range(4):
    try:
        #In this case Selenium lost the object so it's neccesary to search it again. This is due to the page changing our path after interacting with it.
        search_xpath = "//div[@class='headerSup']//input[@class='input']"
        search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
        search_bar = driver.find_element(By.XPATH, search_xpath)
        
        #Here we delete the previous search
        search_bar.send_keys(Keys.CONTROL, 'a')
        search_bar.send_keys(Keys.BACKSPACE)

        #We write our new search
        search_bar.send_keys(productos[i] + ' ' + marcas[i])
        search_bar.send_keys(Keys.ENTER)
        
        try:
            time.sleep(1.5)
            xpath_titulo = "//article//p[@class='h4']"
            #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_titulo)))
            titulos = driver.find_elements(By.XPATH, xpath_titulo)
            titulos = [ti.text for ti in titulos]          
        except:
            no_encontrados.append(producto_actual)
            print('error encontrar titulos')
        try:            
            xpath_precio = "//article//p[@class='precio1']"
            #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_precio)))
            precios = driver.find_elements(By.XPATH, xpath_precio)
            precios = [p.text for p in precios]
        except:
            print('EErro al encontrar precios')
        try:
            xpath_link = "//article//a[1]"
            #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_link)))
            links = driver.find_elements(By.XPATH, xpath_link)
            links = [link.get_attribute("href") for link in links] 
        except:
            print('Error al encontrar links')
    except:
        no_encontrados.append(producto_actual)
        print('error bus')
    
driver.quit() 