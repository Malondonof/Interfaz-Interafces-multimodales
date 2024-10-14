import streamlit as st
from PIL import Image
import os

# Definir estilos CSS
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

# Título y contenido HTML
st.markdown('<h1 class="title">THE BEST FESTIVAL IN THE WORLD</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="header" style="background-color: black;">Aquí subiré todo el contenido</h2>', unsafe_allow_html=True)
st.markdown('<p class="content">Hola mi gente, el día de hoy hablaremos de Tomorrowland</p>', unsafe_allow_html=True)

# Ruta a la imagen en la carpeta "Overwatch-pag-main"
image_path = "Overwatch-pag-main/foro.jpg"

# Verificar si el archivo existe antes de abrirlo
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, caption="Tomorrowland")
else:
    st.error(f"El archivo {image_path} no se encuentra.")

# Input de texto
texto = st.text_input("Tienes 20 años y no has conseguido tu boleta, pues qué lástima yo tampoco")
st.write("El texto escrito es:", texto)

# Subheader y columnas
st.subheader("Vamos a probar dos columnas")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Primera columna")
    st.write("¿Qué es una interfaz?")
    resp = st.checkbox("Pregúntale a ChatGPT")
    if resp:
        st.write("Presta atención a la clase")

with col2:
    st.subheader("Segunda columna")
    modo = st.radio("Selecciona los festivales a los que quisieras ir", ("Ritvals", "After Life", "La Solar"))
    if modo == "Ritvals":
        st.write("Es una marca interesante.")
    elif modo == "After Life":
        st.write("Es una marca francesa.")
    elif modo == "La Solar":
        st.write("La marca más vendida en los Estados Unidos.")

# Sidebar con selección
with st.sidebar:
    st.subheader("Decídete de una vez 😎")
    mod_radio = st.radio(
        "Escoge un festival", 
        ("Ritvals", "After Life", "La Solar")
    )
