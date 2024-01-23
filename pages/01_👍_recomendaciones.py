import streamlit as st
import pandas as pd

st.title('Recomendaciones')
st.markdown('***')

if st.checkbox('Trae 5 Recomendaciones con el tema:'):
    st.write('Restaurantes Mexicanos en USA')

df = pd.read_csv('dataset_trabajo.csv')

dim = st.radio('Dataset muestra:', ('Filas','Columnas'),horizontal=True)
col = {"state":"Estado","Name":"Restaurante_Mexicano","Stars":"Estrellas","Valoracion":"Valoracion_Usuario"}

if dim == 'Filas':
    st.write('Registros:',df.shape[0])
else:
    st.write('Columnas de trabajo:',col)

df1 = df[df['Stars']==5][['Name']]

if st.button('Primera Recomendacion'):
    st.write('Los top 5 Restaurantes Mexicanos Mejor Calificados')

est = st.radio('Restaurantes Mexicanos:', ('5 Estrellas','Top 1'),horizontal=True)
if est == '5 Estrellas':
    st.write('Registros:',df1.shape[0])
else:
    st.write(df1.head(1))

if st.button('Top 2 mejor calificado'):
    st.write(df1.head(2))
if st.button('Top 3 mejor calificado'):
    st.write(df1.head(3))
if st.button('Top 4 mejor calificado'):
    st.write(df1.head(4))
if st.button('Top 5 mejor calificado'):
    st.write(df1.head(5))

df2 = df[df['Stars']==5][['Name','state']]

if st.button('Segunda Recomendacion'):
    st.write('Los top 5 Restaurantes Mexicanos Mejor Calificados por Estado')

esp = st.radio('Restaurantes Mexicanos por Estado:', ('5 Estrellas','Top 1'),horizontal=True)
if esp == '5 Estrellas':
    st.write('Registros:',df2.shape[0])
else:
    st.write(df2.head(1))

if st.button('Top 2 mejor calificado por estado'):
    st.write(df2.head(2))
if st.button('Top 3 mejor calificado por estado'):
    st.write(df2.head(3))
if st.button('Top 4 mejor calificado por estado'):
    st.write(df2.head(4))
if st.button('Top 5 mejor calificado por estado'):
    st.write(df2.head(5))

df3 = df[df['Stars']==1][['Name','state']]

if st.button('Tercera Recomendacion'):
    st.write('Los top 5 Restaurantes Mexicanos con Menor Calificacion por Estado')

est = st.radio('Restaurantes Mexicanos por estado:', ('1 Estrella','Top 1'),horizontal=True)
if est == '1 Estrella':
    st.write('Registros:',df3.shape[0])
else:
    st.write(df3.head(1))

if st.button('Top 2 menor calificado'):
    st.write(df3.head(2))
if st.button('Top 3 menor calificado'):
    st.write(df3.head(3))
if st.button('Top 4 menor calificado'):
    st.write(df3.head(4))
if st.button('Top 5 menor calificado'):
    st.write(df3.head(5))

df4 = df[['Name','Valoracion']]

if st.button('Cuarta Recomendacion'):
    st.write('Los top 5 Restaurantes Mexicanos Valorados por el Usuario')

sel = st.radio('Restaurantes Mexicanos:', ('Valoracion Usuario','Top 1'),horizontal=True)
if sel == 'Valoracion Usuario':
    st.write('Registros:',df4.shape[0])
else:
    st.write(df4.head(1))

if st.button('Top 2 valorado'):
    st.write(df4.head(2))
if st.button('Top 3 valorado'):
    st.write(df4.head(3))
if st.button('Top 4 valorado'):
    st.write(df4.head(4))
if st.button('Top 5 valorado'):
    st.write(df4.head(5))

df5 = df[df['Valoracion']=='Muy bueno'][['Name']]

if st.button('Quinta Recomendacion'):
    st.write('Los top 5 Restaurantes Mexicanos Muy Buenos en USA')

buen = st.radio('Restaurantes Mexicanos:', ('Muy buenos','Top 1'),horizontal=True)
if buen == 'Muy buenos':
    st.write('Registros:',df5.shape[0])
else:
    st.write(df5.head(1))

if st.button('Top 2 muy bueno'):
    st.write(df5.head(2))
if st.button('Top 3 muy bueno'):
    st.write(df5.head(3))
if st.button('Top 4 muy bueno'):
    st.write(df5.head(4))
if st.button('Top 5 muy bueno'):
    st.write(df5.head(5))

