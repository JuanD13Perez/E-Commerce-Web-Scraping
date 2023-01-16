datos = []
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.liverpool.com.mx/tienda/home")
no_encontrados = []

for i in range(len(productos)):
    try:
        search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='form-control search-bar plp-no__results']")))
        #search_bar = driver.find_element(By.CLASS_NAME, "form-control search-bar plp-no__results")
        
        #Here we delete the previous search
        search_bar.send_keys(Keys.CONTROL, 'a')
        time.sleep(0.5) # This page needs some time to load.
        search_bar.send_keys(Keys.BACKSPACE)
        
        #We write our query
        search_bar.send_keys(productos[i])
        search_bar.send_keys(Keys.ENTER)
        
        try:       
            time.sleep(2) # To reload the poge needs aprox this time
            xpath_titulo = "//h1[@class='a-product__information--title']"
            titulo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_titulo)))
            titulo = driver.find_element(By.XPATH, xpath_titulo)
            titulo = [titulo.text]
            
            
            xpath_precio = "//p[@class = 'a-product__paragraphDiscountPrice m-0 d-inline ']"
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_precio)))
            precio = driver.find_element(By.XPATH, xpath_precio)
            precio = [precio.text]
            
            
            get_url = driver.current_url
            link = [str(get_url)]

            # Añadimos el producto con datos np.Nan
            df = pd.DataFrame({'titles': titulo, \
                               'prices': precio, \
                               'links': link, \
                               'id': [productos[i]]}) 
            datos.append(df)

        except:
            # Si este xpath existe es poque la búsqueda devolvió nada.
            nada_xpath = "//div[@class='o-content__noResultsNullSearch']//p[@class = 'o-nullproduct-query'][1]"
            nada = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, nada_xpath))) 
            # Añadimos el producto con datos np.Nan
            df = pd.DataFrame({'titles': [np.nan], \
                               'prices': [np.nan], \
                               'links': [np.nan], \
                               'id': [productos[i]]}) 
            datos.append(df)
    except:
        no_encontrados.append(productos[i])

driver.quit() 
datos_final = pd.concat(datos, ignore_index = True)
datos_final.to_csv('scrapped_csv/Liverpool.csv')