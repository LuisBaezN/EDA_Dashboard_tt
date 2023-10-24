import pandas as pd
import plotly.express as px
import streamlit as st

data = pd.read_excel('data.xlsx') # leer los datos

st.header('Vizualización de datos')
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de los ingresos de medicamentos.')
    
    # crear un histograma
    fig = px.histogram(data, x=' Medication Revenue ')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)