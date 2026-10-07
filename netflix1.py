import streamlit as st
import pandas as pd

st.title("Netflix App")

sidebar = st.sidebar
sidebar.title("Menú y Datos")

sidebar.write("**Integrantes del equipo:**")
sidebar.write("- Jesús Gael Sandoval Rosas (s26004661)")
sidebar.write("- Ángel Josué Aguilar Tepole (s26004562)")
sidebar.write("- Diego Aarón Cruz Guarneros (s26004602)")
sidebar.write("---")

# Cargar datos
URL = "https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv"
dataframe = pd.read_csv(URL, encoding='latin-1')

sidebar.header("Buscador de películas")
myname = sidebar.text_input('Escribe el nombre:')

if sidebar.button('Buscar'):
    sidebar.write(f"Buscando: {myname}")
    
    filtered_by_name = dataframe[dataframe['name'] == myname]
  
    st.header(f"Resultados para: {myname}")
    st.dataframe(filtered_by_name)
else:
    st.write("Usa la barra lateral de la izquierda para buscar una película.")