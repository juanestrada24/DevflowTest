# DevFlow App - Página Principal
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="DevFlow",
    page_icon="🌐",
    layout="wide"
)

# CSS personalizado para estilos visuales, fondo azul oscuro
st.markdown("""
    <style>
        .stApp {
            background: #182848;  /* Azul oscuro */
        }
        .main-title {
            text-align: center;
            color: #ffffff;
            font-size: 3rem;
            margin-bottom: 0.5em;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            color: #bcdff1;
            font-size: 1.5rem;
            margin-bottom: 2em;
        }
        /* NO ocultar el menú lateral para que aparezcan las páginas */
    </style>
""", unsafe_allow_html=True)

# Título principal y subtítulo con estilos
st.markdown('<div class="main-title">Bienvenido a DevFlow</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Dealflow y recursos para constructores</div>', unsafe_allow_html=True)

# Continúa con el resto de tu app aquí...
