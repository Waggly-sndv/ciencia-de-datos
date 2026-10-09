import streamlit as st
import pandas as pd

st.title("Netflix App")

sidebar = st.sidebar
sidebar.title("Menú y Filtros")

sidebar.write("**Integrantes del equipo:**")
sidebar.write("- Jesús Gael Sandoval Rosas (s26004661)")
sidebar.write("- Ángel Josué Aguilar Tepole (s26004562)")
sidebar.write("- Diego Aarón Cruz Guarneros (s26004602)")

URL = "https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/movies.csv"
dataframe = pd.read_csv(URL, encoding='latin-1')

sidebar.header("Buscador por nombre")
myname = sidebar.text_input('Escribe el nombre:')

if sidebar.button('Buscar'):
    sidebar.write(f"Buscando: {myname}")
    filtered_by_name = dataframe[dataframe['name'] == myname]
    st.header(f"Resultados para: {myname}")
    st.dataframe(filtered_by_name)

sidebar.write("---")

sidebar.header("Filtrar por Director")
selected_director = sidebar.selectbox("Selecciona un director", dataframe['director'].unique())

sidebar.write(f"Director seleccionado: {selected_director}")
filtered_data_director = dataframe[dataframe['director'] == selected_director]

st.header(f"Películas dirigidas por: {selected_director}")
st.dataframe(filtered_data_director)