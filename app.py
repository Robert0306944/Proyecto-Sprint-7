import pandas as pd
import streamlit as st
import plotly.graph_objects as go # Importación de plotly.graph_objects como go
# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

#Crear titulo

with st.container():
    st.header('Proyecto Sprint 7')
    st.title('Análisis exploratorio de datos')
    st.write('Click para crea un histograma o gráfico de dispersión de forma interactiva')


#********************************************
# Crear un botón en la aplicación Streamlit
#********************************************

hist_button = st.button('Histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

#********************************************
# Crear un botón 2 en la aplicación Streamlit
#********************************************

graf_dispersion = st.button('Gráfico Dispersion')

# Lógica a ejecutar cuando se hace clic en el botón
if graf_dispersion:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de venta de coches')

    # Crear un scatter plot utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de scatter
    fig_2 = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig_2.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig_2, use_container_width=True)

with st.container():
    st.write('Click en la casilla para crea un histograma o gráfico de dispersión de forma interactiva')

#********************************************
# Crear check 1 en la aplicación Streamlit
#********************************************

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    
    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig_3 = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig_3.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig_3, use_container_width=True)

#********************************************
# Crear check 2 en la aplicación Streamlit
#********************************************

# crear una casilla de verificación
build_graf_disp = st.checkbox('Gráfico de dispersion')

if build_graf_disp: # si la casilla de verificación está seleccionada
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de venta de coches')
    
    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de grafico de dispersion
    fig_4 = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig_4.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig_4, use_container_width=True)
