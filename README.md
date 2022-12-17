# E-commerce Web Scraping

- [**English Version**](#Video)
- [**Spanish Version**](#Spanish-Version)


## Spanish Version

## Business Problem 📝💹

En este proyecto trabajamos para una compañía de e-commerce que se prepara para un fin de semana de promociones. Como tarea nos fue asignado averigüar los precios que maneja la competencia de algunos productos especiales. Nuestro objetico es **determinar el precio mínimo** que maneja la competencia para cada producto para así poder igualarlo. También queremos los nombres, y los links de la competencia. 

**Nota** Todos los scripts se corrieron en un entorno virtual.

Stakeholders: 
* Marketing manager

Recibimos:
* Un archivo de excel (Products_and_comp.xlsx) con una lista de los productos sobre los cuales debemos hacer web scraping.
* Los nombres de las compañías que son competencia y sobre las cuales debemos ingresar a su portal de e-commerce.

Entregable:
* Un pandas dataFrame con los precios y los URL de los productos para cada compañía de la competencia.

A continuación un video con la implementación del algortimo:

### Video
<div align ="center">
    <video src="Video.mp4" width=400/>
<div/>

Cortamos unas partes y aceleramos. Vemos que el algoritmo no es muy rápido ya que usa Selenium. Tampoco pretendemos tener un alto uso de banda ancha. Sobre el final del video vemos los resultados para un test de los primeros 18 links: Un pandas DataFrame con los nombres, links y precios que salen al realizar la búsqueda conjuntamente con un id.


## Requerimientos
 Usamos Python 3.10
 ```
 pandas
 selenium (versión >= 4.3.0)
 ```