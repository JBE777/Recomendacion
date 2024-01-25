import streamlit as st
import pandas as pd

st.subheader("Sistema de recomendaciones")

if st.button('Recomendaciones en:'):
    st.write('Restaurantes Mexicanos en USA')

df = pd.read_csv('archivo_trabajo.csv')

dim = st.radio('Dataset muestra:', ('Filas','Columnas'),horizontal=True)
col={"Name":"Restaurante_Mexicano","state":"Estado",'City':'Ciudad','Address':'Dirección',"Stars":"Estrellas","Valoración":"Valoracion_Usuario"}

if dim == 'Filas':
    st.write('Registros:',df.shape[0],df.head())
else:
    st.write('Columnas de trabajo:',df.shape[1],col)


df['Cantidad_Restaurantes'] = df['state']
df1 = df[df['Stars']==5][['Name','Cantidad_Restaurantes']].groupby(['Name']).count().sort_values(by='Cantidad_Restaurantes',ascending=False)
df1.reset_index(inplace=True)

if st.button('Primera Recomendación'):
    st.write('Top 5 de mayor calificación de los restaurantes mexicanos de los estados')
else:
    st.write('Lista generada filtrando por 5 estrellas')

est = st.radio('Restaurantes Mexicanos:', ('Mejores','Porcentaje'),horizontal=True)
if est == 'Mejores':
    st.write('Registros:', df1.shape[0])
else:
    st.write('Mejores restaurantes',(df1.shape[0]/df.shape[0])*100, '%')

if st.button('Top 5 de mayor calificación de los estados'):
    st.write(df1.head(5))

df['Cantidad_Restaurantes'] = df['state']
df2= df[df['Stars']==5][['Name','state','Cantidad_Restaurantes']].groupby(['Name','state']).count().sort_values(by='Cantidad_Restaurantes',ascending=False)
df2.reset_index(inplace=True)

if st.button('Segunda Recomendación'):
    st.write('Top 5 con mayor calificación de restaurantes mexicanos por estados')
else:
    st.write('Lista generada filtrando por 5 estrellas y estado')

esp = st.radio('Restaurantes Mexicanos:', ('5 Estrellas','Porcentaje'),horizontal=True)
if esp == '5 Estrellas':
    st.write('Registros:', df2.shape[0])
else:
    st.write('Mejores restaurantes por estado',round((df2.shape[0]/df.shape[0])*100,2), '%')

if st.button('Top 5 de mayor calificación por estados'):
    st.write(df2.head(5))

df3 = df[df['Stars']==1][['Name','state','Cantidad_Restaurantes']].groupby(['Name','state']).count().sort_values(by='Cantidad_Restaurantes',ascending=False)
df3.reset_index(inplace=True)

if st.button('Tercera Recomendación'):
    st.write('Top 5 con menor calificación de restaurantes mexicanos por estado')
else:
    st.write("Lista generada filtrando por 1 estrella y estado")

esp = st.radio('Restaurantes Mexicanos:', ('1 Estrella','Porcentaje'),horizontal=True)
if esp == '1 Estrella':
    st.write('Registros:',df3.shape[0])
else:
    st.write('Menor calificación',round((df3.shape[0]/df.shape[0])*100,2), '%')

if st.button('Top 5 con menor calificación por estado'):
    st.write(df3.head(5))

