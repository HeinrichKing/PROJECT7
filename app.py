import os
import pandas as pd
import plotly.express as px
import streamlit as st

current_directory = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_directory, "vehicles_us.csv")

car_data = pd.read_csv(csv_path)
hist_checkbox = st.checkbox('Construir histograma') # crear un botón
scater_checkbox= st.checkbox("Contruir gráfico de dispersión")
        
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
    
if __name__ == "__main__":
    st.run(port=port, server_address="0.0.0.0")