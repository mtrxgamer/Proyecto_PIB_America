import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('pib.csv')

# Filtrar los países de América del CSV
america = [
    'Antigua y Barbuda', 'Argentina', 'Bahamas', 'Barbados', 
    'Belice', 'Bolivia', 'Brasil', 'Canadá', 'Chile', 
    'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Ecuador', 
    'El Salvador', 'Estados Unidos', 'Granada', 'Guatemala', 
    'Guyana', 'Haití', 'Honduras', 'Jamaica', 'México', 'Nicaragua', 
    'Panamá', 'Paraguay', 'Perú', 'República Dominicana', 
    'San Vicente y las Granadinas', 'Santa Lucía', 'Suriname', 
    'Trinidad y Tobago', 'Uruguay', 'Venezuela'
]

# Filtrar el DataFrame para incluir solo los países de América
df_america = df[df["Country Name"].isin(america)]

st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnoKlgMPBv8-ubElsznkUpGZZyTMvkzgiYjsSHvRzqsw&s')

st.subheader('introducción a la programación con Python y R')

st.sidebar.subheader("Dashboard interactivo")

# Selección de país
pais = st.sidebar.selectbox(
    "Seleccione un país",
    df_america["Country Name"].unique()
)

# Selección de rango de años
years = df_america.columns[3:]

st.subheader("Seleccione el rango de años")

# filtro de años con un slider
inicio, fin = st.select_slider(
    "",
    options=list(years),
    value=(years[0], years[-1])
)

y = df_america[
    df_america["Country Name"] == pais
][years].values.flatten()

# Filtrar los datos según el rango de años seleccionado
indice_inicio = list(years).index(inicio)
indice_fin = list(years).index(fin)

x = years[indice_inicio:indice_fin + 1]
y = y[indice_inicio:indice_fin + 1]

# Crear gráfico de línea
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(
    x,
    y,
    marker='o',
    linewidth=2,
    color='blue'
)

ax.set_title(f"PIB (% anual) de {pais}")
ax.set_xlabel("Año")
ax.set_ylabel("PIB (%)")
ax.grid(True)

plt.xticks(rotation=45)

st.pyplot(fig)

# Mostrar métricas de PIB del país, PIB global y diferencia
col1, col2, col3 = st.columns(3)

pib_pais = round(np.nanmean(y), 2)

with col1:
    st.metric(
        label="PIB del país",
        value=f"{pib_pais:.2f}%"
    )

datos_globales = df_america[years].iloc[:, indice_inicio:indice_fin+1]

pib_global = round(
    np.nanmean(datos_globales.values),
    2
)

with col2:
    st.metric(
        label="PIB Global",
        value=f"{pib_global:.2f}%"
    )

diferencia = round(
    pib_pais - pib_global,
    2
)

with col3:
    st.metric(
        label="Diferencia",
        value=f"{diferencia:.2f} %",
        delta=f"{diferencia:.2f}"
    )