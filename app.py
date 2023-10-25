import pandas as pd
import plotly.express as px
import streamlit as st

def plot_hist(title, row):
    st.write(title)
    
    fig = px.histogram(data, x=row)

    st.plotly_chart(fig, use_container_width=True)

data = pd.read_excel('data.xlsx')
data.columns = list(data.columns.str.strip())

data['Lab Cost'] = data['Lab Cost'].replace(' $-   ', '0').astype(float)

st.header('Vizualización de datos')

st.subheader('Estructura')
st.write(data.head(3))

st.write('Seleccione los datos que desee vizualizar en un histograma')
form = st.form("checkboxes", clear_on_submit=True)
with form:
    med_rev = st.checkbox("Ganancias en medicamentos")
    lab_cost = st.checkbox("Costo de laboratorios")
    con_rev = st.checkbox("Ganancias en consulta")

submit = form.form_submit_button("Enviar")

if med_rev:
    plot_hist('Ganancias en medicamentos', 'Medication Revenue')

if lab_cost:
    plot_hist('Costo de laboratorios', 'Lab Cost')

if con_rev:
    plot_hist('Ganancias en consulta', 'Consultation Revenue')

st.subheader("Ganancias")
hist_button = st.button('Vizualizar')

if hist_button:
    st.write('Ganancias de consultas contra medicamentos')
    
    fig = px.scatter(data, x='Consultation Revenue', y='Medication Revenue')
    st.plotly_chart(fig, use_container_width=True)