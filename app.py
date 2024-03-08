import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Creacion de graficos') #crear encabezado

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un boton
scatter_button = st.button('Construir gráfico de dispersión') # crear otro botón

if hist_button: # al hacer clic en el boton
    # escribir un mensaje
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un grafico Ploty interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button: # al hacer clic en el segundo botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)