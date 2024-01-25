import streamlit as st
import time

col1,col2,col3 = st.columns([1,2,1])

col1.markdown(" ## Welcome to my app! ")
col2.markdown(" ### Recomendaciones")

uploaded_photo = col2.file_uploader("Upload a photo")
camera_photo = col2.camera_input("Take a photo")

progress_bar = col2.progress(0)

for perc_completed in range(100):
    time.sleep(0.5)
    progress_bar.progress(perc_completed+1)

col2.success("Photo uploaded successfully")



