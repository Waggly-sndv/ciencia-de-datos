import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

titanic_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(titanic_data)
st.header("Data Description")

fig, ax = ptl.subplots()
ax.hits(titanic_data.fare)
st.header("Histograma del Titanic")
st.pyplot(fig)