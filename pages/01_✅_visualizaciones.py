import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if st.checkbox('Visual de Recomendaciones'):
    st.write('Restaurantes Mexicanos en USA')

df = pd.read_csv('dataset_trabajo.csv')

dim = st.radio('Dataset muestra:', ('Filas','Columnas'),horizontal=True)
Col = {"state":"Nombre_Estado","Name":"Nombre_Restaurante","Stars":"Numero_Estrellas","Valoracion":"Valoracion_Usuario"}

if dim == 'Filas':
    st.write('Registros:',df.shape[0])
else:
    st.write('Columnas involucradas:',Col)

df1 = df[df['Stars']==5][['Name']]
RM = df1[df1["Name"].isin(["Corazon Cocina","Nada","Pueblo Lindo","Loco Mexican Restaurant & Cantina",
"Taqueria Don Quezadillas Belinda"])]

if st.button('Primera Recomendacion'):
    st.write(df1[:5])
else:
    st.write('Top 5 Restaurantes Mexicanos Mejor Calificados')

if st.button('Restaurantes 5 Estrellas'):
    st.write('Registros:',df1.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Name',color='#0CF926',data=RM)
plt.ylabel('Restaurantes')
plt.xlabel('Cantidad')
st.pyplot(fig)

df2 = df[df['Stars']==5][['Name','state']]

state = df[df['state'].isin(["California","Indiana","Idaho","Indiana","Indiana"])]

if st.button('Segunda Recomendacion'):
        st.write(df2[:5])
else:
    st.write('Top 5 Restaurantes Mexicanos Mejor Calificados por Estado')

if st.button('Restaurantes 5 Estrellas por Estado'):
    st.write('Registros:',df2.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='state',color='#0CF926',data=state)
plt.ylabel('Estados de USA')
plt.xlabel('Cantidad')
st.pyplot(fig)

df3 = df[df['Stars']==1][['Name','state']]

RM_1 = df[df['Name'].isin(["Taco Bell","Que Pasa Mexican Cantina","Buena Onda","Moe's Southwest Grill","Uncle Julio's"])]

if st.button('Tercera Recomendacion'):
        st.write(df3[:5])
else:
    st.write('Top 5 Restaurantes Mexicanos con Menor Calificacion por Estado')

if st.button('Restaurantes Mexicanos 1 Estrella'):
    st.write('Registros:',df3.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Name',color='#0CF926',data=RM_1)
plt.ylabel('Restaurantes')
plt.xlabel('Cantidad')
st.pyplot(fig)
        
state1 = df[df['state'].isin(["Missouri","Florida","Pensilvania","Nueva Jersey","Tennessee"])]

if st.button('Restaurantes Mexicanos 1 Estrella por Estado'):
    st.write('Registros:',df3.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='state',color='#0CF926',data=state1)
plt.ylabel('Estados de USA')
plt.xlabel('Cantidad')
st.pyplot(fig)

df4 = df[['Name','Valoracion']]

if st.button('Cuarta Recomendacion'):
        st.write(df4[:5])
else:
    st.write('Top 5 Restaurantes Mexicanos Valorados por el Usuario')

if st.button('Valoracion Usuario'):
    st.write('Registros:',df4.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Valoracion',color='#0CF926',data=df4)
plt.ylabel('Valoracion del cliente')
plt.xlabel('Cantidad')
st.pyplot(fig)

df5 = df[df['Valoracion']=='Muy bueno'][['Name']]
df6 = df5[df5['Name'].isin(["Jimmy Hula's","GUAC Tequila & Tacos","Corazon Cocina","Zeppelin","Nada"])]

if st.button('Quinta Recomendacion'):
        st.write(df5[:5])
else:
    st.write('Top 5 Restaurantes Mexicanos Muy Buenos en USA')

if st.button('Muy Buenos Restaurantes Mexicanos'):
    st.write('Registros:',df6.shape[0])

fig = plt.figure(figsize=(4,2))
sns.countplot(y='Name',color='#0CF926',data=df6)
plt.ylabel('Restaurantes')
plt.xlabel('Cantidad')
st.pyplot(fig)
