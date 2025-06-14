# DevFlow App - Página Principal

`import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="DevFlow",
    page_icon="🌐",
    layout="wide"
)

# Inyectar CSS personalizado y botón hamburguesa con JS para mostrar/ocultar el menú lateral
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
        /* Ocultar menú lateral por defecto */
        [data-testid="stSidebarNav"] {
            display: none;
        }
        /* Botón hamburguesa */
        .hamburger {
            position: fixed;
            top: 2rem;
            left: 2rem;
            z-index: 9999;
            cursor: pointer;
            width: 48px;
            height: 48px;
            background: #ffffffcc;
            border-radius: 12px;
            box-shadow: 0 2px 8px #2222;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: background 0.2s;
        }
        .hamburger:hover {
            background: #e0e7efcc;
        }
        .hamburger span, .hamburger span:before, .hamburger span:after {
            content: '';
            display: block;
            background: #1b263b;
            height: 4px;
            width: 30px;
            border-radius: 2px;
            margin: 0 auto;
            transition: 0.3s;
            position: relative;
        }
        .hamburger span:before, .hamburger span:after {
            position: absolute;
            left: 0;
        }
        .hamburger span:before {
            top: -10px;
        }
        .hamburger span:after {
            top: 10px;
        }
    </style>
    <script>
        function toggleSidebar() {
            const sidebar = parent.document.querySelector('[data-testid="stSidebar"]');
            if (sidebar) {
                sidebar.style.display = sidebar.style.display === 'none' ? 'block' : 'none';
            }
        }
    </script>
    <div class="hamburger" onclick="toggleSidebar()">
        <span></span>
    </div>
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
