import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Minecraft")

url = "https://raw.githubusercontent.com/Waggly-sndv/Minecraft-dataset/refs/heads/main/example.json"
df = pd.read_json(url)

df['largo_texto'] = df['instruction'].apply(str).apply(len)
df['largo_respuesta'] = df['output'].apply(str).apply(len)

categorias = []
for t in df['instruction']:
    t_str = str(t).lower()
    if 'food' in t_str or 'cake' in t_str or 'wheat' in t_str:
        categorias.append('comida')
    else:
        categorias.append('otros')
df['categoria'] = categorias

df['tamano'] = ['largo' if x > 50 else 'corto' for x in df['largo_respuesta']]

st.sidebar.write("Controles")

buscar = st.sidebar.text_input("Buscar texto")

filtro_num = st.sidebar.slider("Filtro slider", 0, 500, 500)
filtro_cat = st.sidebar.radio("Filtro radio", ['Todas', 'comida', 'otros'])
filtro_tam = st.sidebar.selectbox("Filtro lista", ['Todos', 'corto', 'largo'])

df2 = df.copy()

if buscar != "":
    df2 = df2[df2['instruction'].str.contains(buscar, case=False, na=False)]

df2 = df2[df2['largo_texto'] <= filtro_num]

if filtro_cat != 'Todas':
    df2 = df2[df2['categoria'] == filtro_cat]

if filtro_tam != 'Todos':
    df2 = df2[df2['tamano'] == filtro_tam]

if st.checkbox("Mostrar dataset"):
    st.dataframe(df2)

st.write("Grafica 1")
fig1, ax1 = plt.subplots()
ax1.hist(df2['largo_texto'], bins=15)
ax1.set_xlabel("Largo del texto")
ax1.set_ylabel("Cantidad")
st.pyplot(fig1)

st.write("Grafica 2")
fig2, ax2 = plt.subplots()
conteos = df2['categoria'].value_counts()
ax2.barh(conteos.index, conteos.values)
ax2.set_xlabel("Cantidad")
ax2.set_ylabel("Categoria")
st.pyplot(fig2)

st.write("Grafica 3")
fig3, ax3 = plt.subplots()
ax3.scatter(df2['largo_texto'], df2['largo_respuesta'])
ax3.set_xlabel("Largo de instruccion")
ax3.set_ylabel("Largo de respuesta")
st.pyplot(fig3)

st.write("Acerca de")
st.write("Autor: Jesús Gael Sandoval Rosas")
st.write("Matricula: s26004661")

mapa = pd.DataFrame({'lat': [18.8497], 'lon': [-97.1036]})
st.map(mapa)