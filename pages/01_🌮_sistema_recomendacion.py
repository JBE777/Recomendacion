import streamlit as st
import pandas as pd

st.subheader("Sistema de recomendaciones")

if st.button('Recomendaciones con el tema:'):
    st.write('Restaurantes Mexicanos en USA')

df = pd.read_csv('archivo_trabajo.csv')

dim = st.radio('Dataset muestra:', ('Filas','Columnas'),horizontal=True)
col={"Name":"Restaurante_Mexicano","state":"Estado",'City':'Ciudad','Address':'Direccion',"Stars":"Estrellas","Valoracion":"Valoracion_Usuario"}

if dim == 'Filas':
    st.write('Registros:',df.shape[0])
else:
    st.write('Columnas de trabajo:',col)


df['Cantidad_USA'] = df['state']
df1 = df[df['Stars']==5][['Name','Cantidad_USA']].groupby(['Name']).count().sort_values(by='Cantidad_USA',ascending=False)
df1.reset_index(inplace=True)

if st.button('Primera Recomendacion'):
    st.write('Los top 5 Mejores Restaurantes Mexicanos en USA')
else:
    st.write('Lista generada filtrando por 5 estrellas')

est = st.radio('Restaurantes Mexicanos:', ('Mejores','Porcentaje'),horizontal=True)
if est == 'Mejores':
    st.write('Registros:',df1.shape[0])
else:
    st.write('Mejores restaurantes',(df1.shape[0]/df.shape[0])*100, '%')

if st.button('Top 5 Mejores Restaurantes'):
    st.write(df1.head(5))

df['Cantidad_Restaurantes'] = df['state']
df2= df[df['Stars']==5][['Name','state','Cantidad_Restaurantes']].groupby(['Name','state']).count().sort_values(by='Cantidad_Restaurantes',ascending=False)
df2.reset_index(inplace=True)

if st.button('Segunda Recomendacion'):
    st.write('Los top 5 Mejores Restaurantes Mexicanos en USA por estado')
else:
    st.write('Lista generada filtrando por 5 estrellas y estado')

esp = st.radio('Restaurantes Mexicanos:', ('5 Estrellas','Porcentaje'),horizontal=True)
if esp == '5 Estrellas':
    st.write('Registros:',df2.shape[0])
else:
    st.write('Mejores restaurantes por estado',round((df2.shape[0]/df.shape[0])*100,2), '%')

if st.button('Top 5 Mejores restaurantes por estado'):
    st.write(df2.head(5))

df3 = df[df['Stars']==4][['Name','state','Cantidad_Restaurantes']].groupby(['Name','state']).count().sort_values(by='Cantidad_Restaurantes',ascending=False)
df3.reset_index(inplace=True)

if st.button('Tercera Recomendacion'):
    st.write("Los top 5 Restaurantes Mexicanos en USA con Buena Valoracion")
else:
    st.write("Lista generada filtrando por 4 estrellas y estado")

esp = st.radio('Restaurantes Mexicanos:', ('4 Estrellas','Porcentaje'),horizontal=True)
if esp == '4 Estrellas':
    st.write('Registros:',df3.shape[0])
else:
    st.write('Buena valoracion',round((df3.shape[0]/df.shape[0])*100,2), '%')

if st.button('Top 5 Buena valoracion'):
    st.write(df3.head(5))

df4 = df[df['Stars']==1][['Name','state','Cantidad_Restaurantes']].groupby(['Name','state']).count().sort_values(by='Cantidad_Restaurantes',ascending=False)
df4.reset_index(inplace=True)

if st.button('Cuarta Recomendacion'):
    st.write('Los top 5 Restaurantes Mexicanos en USA Peor Calificados por estado')
else:
    st.write("Lista generada filtrando por 1 estrella y estado")

est = st.radio('Restaurantes Mexicanos:', ('1 Estrella','Porcentaje'),horizontal=True)
if est == '1 Estrella':
    st.write('Registros:',df4.shape[0])
else:
    st.write('Peor calificados por estado',round((df4.shape[0]/df.shape[0])*100,2), '%')

if st.button('Top 5 Peor calificados por estado'):
    st.write(df4.head(5))
