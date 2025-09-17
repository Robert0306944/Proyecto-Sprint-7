# Proyecto-Sprint-7
Proyecto sobre herramientas del desarrollo del software

### Configuración 

- Se realiza un análisis exploratorio de datos.
- Se instaló los paquetes pandas, y plotly.
- Adicional el paquete streamlit para desarrollar una aplicación web.
- Se Creó un nuevo entorno virtual llamado vehículos.
- Se clonó el repositorio del proyecto desde GitHub y posterior se lo ábre como un proyecto en VS Code.


### Análisis exploratorio de datos

- Se creó una carpeta llamada notebooks
- Con Jupyter Notebooks se creo un archivo llamado EDA.ipynb
- En EDA.ipynb se experimentó con el paquete plotly para crear visualizaciones para el análisis exploratorio.
- Se creó un histograma y un gráfico de dispersión.

### Desarrollo del cuadro de mandos de la aplicación web

- Se crea un archivo llamado app.py en la raíz del directorio del proyecto.
- Importamos los paquetes (streamlit como st, pandas y plotly).
- Leemos el archivo CSV del conjunto de datos en un DataFrame.
- Creamos la aplicación basada en Streamlit: 
-Con un encabezado
-Con 2 botones un que cree un histogramas y el otro un gráfico de dispersion
-De igual manera casillas de verificación para cada uno.

### Despliegue de la versión final de la aplicación en Render

- Con Render
- Creamos un nuevo servicio web enlazado a tu repositorio de Github.
- Desplegamos en Render y espera a que el build se ejecute con éxito.
