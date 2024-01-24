import streamlit as st
import pandas as pd

st.title('Recomendaciones')
st.markdown('***')

if st.checkbox('Trae 4 Recomendaciones con el tema:'):
    st.write('Restaurantes Mexicanos en USA')

df = pd.read_csv('archivo_trabajo.csv')

dim = st.radio('Dataset muestra:', ('Filas','Columnas'),horizontal=True)
col={"Name":"Restaurante_Mexicano","state":"Estado",'City':'Ciudad','Address':'Direccion',"Stars":"Estrellas","Valoracion":"Valoracion_Usuario"}

if dim == 'Filas':
    st.write('Registros:',df.shape[0])
else:
    st.write('Columnas de trabajo:',col)

df1 = df[['Name','state','City','Address','Stars','Valoracion']]

if st.button('Primera Recomendacion'):
    st.write('Los top 5 Restaurantes Mexicanos en USA')

est = st.radio('Restaurantes Mexicanos:', ('Estandar','Porcentaje'),horizontal=True)
if est == 'Estandar':
    st.write('Registros:',df1.shape[0])
else:
    st.write('Total datos',(df1.shape[0]/df.shape[0])*100, '%')

if st.button('Top 1 Restaurantes Mexicanos en USA'):
    st.write(df1.head(1))   
if st.button('Top 2 Restaurantes Mexicanos en USA'):
    st.write(df1.head(2))
if st.button('Top 3 Restaurantes Mexicanos en USA'):
    st.write(df1.head(3))
if st.button('Top 4 Restaurantes Mexicanos en USA'):
    st.write(df1.head(4))
if st.button('Top 5 Restaurantes Mexicanos en USA'):
    st.write(df1.head(5))

df2 = df[df['Stars']==5][['Name','state','City','Address','Valoracion']]

if st.button('Segunda Recomendacion'):
    st.write("Los top 5 Restaurantes Mexicanos en USA Mejor Calificados")

esp = st.radio('Restaurantes Mexicanos:', ('5 Estrellas','Porcentaje'),horizontal=True)
if esp == '5 Estrellas':
    st.write('Registros:',df2.shape[0])
else:
    st.write('Mejor calificados',(df2.shape[0]/df.shape[0])*100, '%')

if st.button('Top 1 Mejor calificados'):
    st.write(df2.head(1))
if st.button('Top 2 Mejor calificados'):
    st.write(df2.head(2))
if st.button('Top 3 Mejor calificados'):
    st.write(df2.head(3))
if st.button('Top 4 Mejor calificados'):
    st.write(df2.head(4))
if st.button('Top 5 Mejor calificados'):
    st.write(df2.head(5))

df3 = df[df['Stars']==4][['Name','state','City','Address','Valoracion']]

if st.button('Tercera Recomendacion'):
    st.write("Los top 5 Restaurantes Mexicanos en USA Buena Valoracion")

esp = st.radio('Restaurantes Mexicanos:', ('4 Estrellas','Porcentaje'),horizontal=True)
if esp == '4 Estrellas':
    st.write('Registros:',df3.shape[0])
else:
    st.write('Buena valoracion',round((df3.shape[0]/df.shape[0])*100,2), '%')

if st.button('Top 1 Buena valoracion'):
    st.write(df3.head(1))
if st.button('Top 2 Buena valoracion'):
    st.write(df3.head(2))
if st.button('Top 3 Buena valoracion'):
    st.write(df3.head(3))
if st.button('Top 4 Buena valoracion'):
    st.write(df3.head(4))
if st.button('Top 5 Buena valoracion'):
    st.write(df3.head(5))

df4 = df[df['Stars']==1][['Name','state','City','Address','Valoracion']]

if st.button('Cuarta Recomendacion'):
    st.write('Los top 5 Restaurantes Mexicanos en USA Peor Calificados')

est = st.radio('Restaurantes Mexicanos:', ('Peor calificados','Porcentaje'),horizontal=True)
if est == 'Peor calificados':
    st.write('Registros:',df4.shape[0])
else:
    st.write('Peor calificados',round((df4.shape[0]/df.shape[0])*100,2), '%')

if st.button('Top 1 Peor calificados'):
    st.write(df4.head(1))
if st.button('Top 2 Peor calificados'):
    st.write(df4.head(2))
if st.button('Top 3 Peor calificados'):
    st.write(df4.head(3))
if st.button('Top 4 Peor calificados'):
    st.write(df4.head(4))
if st.button('Top 5 Peor calificados'):
    st.write(df4.head(5))



