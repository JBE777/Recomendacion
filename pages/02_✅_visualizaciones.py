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

if dim == 'Filas':
    st.write('Registros:',df.shape[0])
else:
    st.write('Columnas:',df.shape[1])

if st.button('Estrellas en Restaurantes Mexicanos de USA'):
    st.write('Registros',df.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Stars',color='#75FA61',data=df)
plt.ylabel('Estrellas',fontsize=5)
plt.xlabel('Cantidad de estrellas',fontsize=5)
st.pyplot(fig)

if st.button('Valoración de Restaurantes Mexicanos de USA'):
    st.write('Registros',df.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Valoracion',color='#75FA61',data=df)
plt.ylabel('Valoración del usuario',fontsize=6)
plt.xlabel('Cantidad de valoraciones',fontsize=6)
st.pyplot(fig)

df['Cantidad_Restaurantes'] = df['state']
df1 = df[df['Stars']==5][['Name','Cantidad_Restaurantes']].groupby(['Name']).count().sort_values(by='Cantidad_Restaurantes',ascending=False)
df1.reset_index(inplace=True)
RM = df[df['Name'].isin(['Los Agaves','Bartaco','Tumerico','Bakersfield','South Philly Barbacoa'])]

if st.button('Los top 5 Mejores Restaurantes Mexicanos de USA'):
    st.write('Registros',df1.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Name',color='#75FA61',data=RM)
plt.ylabel('Restaurantes',fontsize=6)
plt.xlabel('Cantidad de restaurantes',fontsize=6)
st.pyplot(fig)

df2 = df[df['Stars']==5][['Name','state','Cantidad_Restaurantes']].groupby(['Name','state']).count().sort_values(by='Cantidad_Restaurantes',ascending=False)
df2.reset_index(inplace=True)
nom = df[df['Name'].isin(["Los Agaves","Tumerico","South Philly Barbacoa","Zeppelin","Capital Tacos"])]

if st.button('Los top 5 Mejores Restaurantes Mexicanos en USA por estado'):
    st.write('Registros por estado',df2.shape[0])

    st.write('Registros',df1.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Name',color='#75FA61',data=nom)
plt.ylabel('Restaurantes',fontsize=6)
plt.xlabel('Cantidad de restaurantes',fontsize=6)
st.pyplot(fig)

df3 = df[df['Stars']==1][['Name','state','Cantidad_Restaurantes']].groupby(['Name','state']).count().sort_values(by='Cantidad_Restaurantes',ascending=False)
df3.reset_index(inplace=True)
name = df3[df3['Name'].isin(["Chili's","Taco Bell","Taco Bell","Taco Bell","Chipotle Mexican Grill"])]

if st.button('Los top 5 Restaurantes Mexicanos en USA Peor Calificados'):
        st.write('Registros por estado',df3.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Name',color='#75FA61',data=name)
plt.ylabel('Restaurantes',fontsize=6)
plt.xlabel('Cantidad de restaurantes',fontsize=6)
st.pyplot(fig)


