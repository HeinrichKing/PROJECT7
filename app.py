import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Análisis de Anuncios de Venta de Coches")  

current_directory = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_directory, "vehicles_us.csv")

car_data = pd.read_csv(csv_path)
hist_checkbox = st.checkbox('Construir histograma') 
scater_checkbox= st.checkbox("Contruir gráfico de dispersión")
pie_checkbox= st.checkbox("Construir gráfico de pastel")
if hist_checkbox: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivosw
    st.plotly_chart(fig, use_container_width=True)
    
if scater_checkbox:
    
    st.write("Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches")
    
    #Creamos el gráfico de dispersión 
    fig1 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    
    #Mostramos el gráfico de dispersión 
    st.plotly_chart(fig1, use_container_width=True )
    
if pie_checkbox: 
    transmission_counts = car_data['transmission'].value_counts().reset_index()
    transmission_counts.columns = ['transmission', 'count']


    st.write("Grafico de pastel de que porcentaje de vehiculos manejan los diferentes tipos de transmiciones")
    # Crear gráfico de pastel (pie chart)
    fig3 = px.pie(transmission_counts, values='count', names='transmission', title="Distribución de Transmisiones")
    st.plotly_chart(fig3, use_container_width=True )
