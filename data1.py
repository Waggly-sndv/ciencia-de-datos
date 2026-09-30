import pandas as pd
import streamlit as st

names_link ="https://raw.githubusercontent.com/Waggly-sndv/Minecraft-dataset/refs/heads/main/example.json"

names_data = pd.read_json(names_link)

# Create the title for the web app
st.title("Streamlit and pandas by waggly-sndv")

st.dataframe(names_data)