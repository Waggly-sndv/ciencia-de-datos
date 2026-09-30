import streamlit as st
import datetime
import pandas as pd


today = datetime.date.today()
today_date = st.date_input('Current date', today)
st.success('Current date: `%s`' % (today_date))
titanic_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")

st.header("dataset")
agree = st.checkbox("show DataSet Overview 7 ")
if agree:
    st.dataframe(titanic_data)
selected_town = st.radio("Select Embark Town",
titanic_data['embark_town'].unique())
st.write("Selected Embark Town:", selected_town)
st.write(titanic_data.query(f"""embark_town==@selected_town"""))
st.markdown("___")

optionals = st.expander("Optional Configurations", True)
fare_min = optionals.slider(
"Minimum Fare",
min_value=float(titanic_data['fare'].min()),
max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
"Maximum Fare",
min_value=float(titanic_data['fare'].min()),
max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) &
(fare_min <= titanic_data['fare'])]
st.write(f"Number of Records With Fare Between {fare_min} and {fare_max}: {subset_fare.shape[0]}")

st.dataframe(subset_fare)