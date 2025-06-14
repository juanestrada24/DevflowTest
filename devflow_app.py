# DevFlow App - Página Principal
```python name=devflow_app.py
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="DevFlow",
    page_icon="🌐",
    layout="wide"
)

# CSS personalizado para estilos visuales, pero SIN ocultar el menú lateral
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #f0f4f8 0%, #e0e7ef 100%);
        }
        .main-title {
            text-align: center;
            color: #1b263b;
            font-size: 3rem;
            margin-bottom: 0.5em;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            color: #415a77;
            font-size: 1.5rem;
            margin-bottom: 2em;
        }
        .header-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 250px;
            border-radius: 1em;
            margin-bottom: 2em;
            box-shadow: 0 4px 16px #1b263b22;
        }
        /* NO ocultar el menú lateral para que aparezcan las páginas */
    </style>
""", unsafe_allow_html=True)

# Título principal y subtítulo con estilos
st.markdown('<div class="main-title">Bienvenido a DevFlow</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Dealflow y recursos para constructores</div>', unsafe_allow_html=True)

# Imagen destacada (puedes usar tu propia URL o subir una local)
st.markdown(
    '<img src="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=600&q=80" class="header-image"/>',
    unsafe_allow_html=True
)

# Continúa con el resto de tu app aquí...
```
Ahora, el menú lateral de Streamlit (incluyendo el de pages, si usas la carpeta `pages/`) volverá a aparecer y funcionar normalmente.
