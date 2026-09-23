import pandas as pd
import streamlit as st

names_link = "https://colab.research.google.com/drive/1W7AnWgkKUvmOQKPzzf2-02oD5eAlP7er?usp=sharing"

names_data = pd.read_csv(names_link)

# Create the title for the web app
st.title("Streamlit and pandas by waggly-sndv")

st.dataframe(names_data)