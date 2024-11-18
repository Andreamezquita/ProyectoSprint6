import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Creación de diagramas')
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button=st.button('Construir histograma') # Crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig=px.histogram(car_data,x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# construir un grafico de dispersión
disp_button=st.button('Construir un gráfico de dispersión')

if disp_button:
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un grafico de dispersion
    fig2=px.scatter(car_data, x="odometer")

    st.plotly_cart(fig, use_container_width=True)
