import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Visualizaciones')
st.markdown('***')

if st.checkbox('Visual de Recomendaciones'):
    st.write('Restaurantes Mexicanos en USA')

df = pd.read_csv('archivo_trabajo.csv')

dim = st.radio('Dataset muestra:', ('Filas','Columnas'),horizontal=True)
col={"Name":"Restaurante_Mexicano","state":"Estado",'City':'Ciudad','Address':'Direccion',"Stars":"Estrellas","Valoracion":"Valoracion_Usuario"}

if dim == 'Filas':
    st.write('Registros:',df.shape[0])
else:
    st.write('Columnas involucradas:',col)

df1 = df[['Name','state','City','Address','Stars','Valoracion']]
RM = df1[df1["Name"].isin(["Tio Flores","Jimmy Hula's","Taco Bell","Chuy's","GUAC Tequila & Tacos"])]

if st.button('Top 5 Restaurantes Mexicanos de USA Estandar'):
    st.write(df1[:5])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Name',color='#0CF926',data=RM)
plt.ylabel('Restaurantes')
plt.xlabel('Cantidad')
st.pyplot(fig)

if st.button('Estrellas en Restaurantes Mexicanos de USA'):
    st.write('Registros',df1.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Stars',color='#0CF926',data=df1)
plt.ylabel('Estrellas')
plt.xlabel('Cantidad')
st.pyplot(fig)

if st.button('Valoracion de Restaurantes Mexicanos de USA'):
    st.write('Registros',df1.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Valoracion',color='#0CF926',data=df1)
plt.ylabel('Valoracion')
plt.xlabel('Cantidad')
st.pyplot(fig)

df2 = df[df['Stars']==5][['Name','state','City','Address','Valoracion']]

nom = df2[df2['Name'].isin(['Corazon Cocina','Nada','Pueblo Lindo','Loco Mexican Restaurant & Cantina','Taqueria Don Quezadillas Belinda'])]
if st.button('Top 5 Restaurantes Mexicanos en USA Mejor Calificados'):
        st.write(df2[:5])
else:
    st.write('Registros',df2.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Name',color='#0CF926',data=nom)
plt.ylabel('Restaurantes')
plt.xlabel('Cantidad')
st.pyplot(fig)

df3 = df[df['Stars']==4][['Name','state','City','Address','Valoracion']]

RM_1 = df[df['Name'].isin(["Skyline Chili","Chili's","Rocco's Tacos and Tequila Bar - Tampa","Puerto Vallarta Mexican Restaurant & Cantina","Nada"])]

if st.button('Los top 5 Restaurantes Mexicanos en USA Buena Valoracion'):
        st.write(df3[:5])
else:
    st.write('Registros:',df3.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Name',color='#0CF926',data=RM_1)
plt.ylabel('Restaurantes')
plt.xlabel('Cantidad')
st.pyplot(fig)
        

df4 = df[df['Stars']==1][['Name','state','City','Address','Valoracion']]
name = df4[df4['Name'].isin(["Taco Bell","Que Pasa Mexican Cantina","Buena Onda","Moe's Southwest Grill","Uncle Julio's"])]

if st.button('Los top 5 Restaurantes Mexicanos en USA Peor Calificados'):
        st.write(df4[:5])
else:
    st.write('Registros:',df4.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Name',color='#0CF926',data=name)
plt.ylabel('Restaurantes')
plt.xlabel('Cantidad')
st.pyplot(fig)

