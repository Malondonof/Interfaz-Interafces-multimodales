import streamlit as st
from PIL import Image
import os


st.markdown("""
    <style>
    .title {
        font-family: 'Arial', sans-serif;
        color: #2E86C1;
    }
    .header {
        font-family: 'Courier New', Courier, monospace;
        color: #FFFFFF;
    }
    .content {
        font-family: 'Verdana', sans-serif;
        color: #1ABC9C;
    }
    </style>
    """, unsafe_allow_html=True)


st.markdown('<h1 class="title">GET READY TO SAVE THE WORLD</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="header" style="background-color: black;">Aquí subiré todo el contenido</h2>', unsafe_allow_html=True)
st.markdown('<p class="content">Hoy conoceremos mas de overwatch</p>', unsafe_allow_html=True)


image_path = "Overwatch-pag-main/foro.jpg"


if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption="Overwatch")
else:
    st.error(f"El archivo {image_path} no se encuentra.")


texto = st.text_input("Parce, ya en sexto semestre")
st.write("El texto escrito es:", texto)


st.subheader("Prueba de interfaz")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Columna 1")
    st.write("¿En que numero estoy pensando?")
    resp = st.checkbox("2")
    resp2 = st.checkbox("Que se yo mano")
    if resp:
        st.write("Incorrecto ma friend")
    if resp2:
        st.write("Buen punto")

with col2:
    st.subheader("Columna 2")
    modo = st.radio("Cual es tu estilo de juego favorito", ("Healer", "Dps", "Defensa"))
    if modo == "Healer":
        st.write("Call a ambulance, call a ambulance, but not for me.")
    elif modo == "Dps":
        st.write("Pa pa pa pa paaaaaa.")
    elif modo == "Defensa":
        st.write("Muy precavido mi amigo.")


with st.sidebar:
    st.subheader("Escoje tu rol 🦸")
    mod_radio = st.radio(
        "Cual es tu especialidad?", 
        ("Dps", "Tanque", "Apoyo")
    )
