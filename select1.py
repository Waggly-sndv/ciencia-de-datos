import streamlit as st
import pandas as pd
st.title("Titanic Dataset")

data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(data)
selected_sex = st.selectbox("Select Sex", data ['sex'].unique())
st.write(f"Selected Option: {selected_sex!r}")
filtered_data_sex = data[data['sex'] == selected_sex]
st.dataframe (filtered_data_sex)