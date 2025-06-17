# DevFlow App - Página Principal
import streamlit as st
st.write("Versión de Streamlit:", st.__version__)
import pandas as pd
import sqlite3


# Configuración de la página
st.set_page_config(
    page_title="DevFlow - Análisis de Proyecto",
    page_icon="🌐",
    layout="wide"
)

# CSS personalizado para estilos visuales, fondo azul oscuro y títulos centrados
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
        .subtitle, .intro-text {
            text-align: center;
            color: #bcdff1;
            font-size: 1.5rem;
            margin-bottom: 2em;
        }
        .intro-text {
            color: #e0e6ed;
            font-size: 1.2rem;
            margin-bottom: 2em;
            font-weight: 400;
        }
        .center-buttons {
            display: flex;
            justify-content: center;
            gap: 2em;
            margin-bottom: 2em;
        }
        .stButton>button {
            font-size: 1.1rem;
            padding: 0.5em 2em;
        }
    </style>
""", unsafe_allow_html=True)

# Título principal y subtítulo con estilos
st.markdown('<div class="main-title">DevFlow</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">DealFlow para constructores e inversores</div>', unsafe_allow_html=True)

# Texto de introducción
intro = """
Real Estate Deals Underwriting On The Go <br>

<ul style='text-align:center; list-style-position: inside; color: #e0e6ed; font-size: 1.1rem;'>
<li>Automatizamos el análisis financiero de tus proyectos</li>
<li>Comparte oportunidades con profesionales clave de la industria</li>
<li>Coordina la ejecución con flujos colaborativos y seguimiento en tiempo real</li>
</ul>
"""
st.markdown(f'<div class="intro-text">{intro}</div>', unsafe_allow_html=True)

# -------------------------------
# Botones principales centrados
# -------------------------------

import streamlit as st

st.markdown('<div class="center-buttons">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    if st.button("Check Deal"):
        st.switch_page("pages/1_📝_New_Flip.py")
with col2:
    if st.button("Login"):
        st.session_state['page'] = 'login'
        st.info("Redirigir a login (aún no implementado)")

with col3:
    if st.button("Crear cuenta"):
        st.session_state['page'] = 'register'
        st.info("Redirigir a registro (aún no implementado)")

st.markdown('</div>', unsafe_allow_html=True)

# Formulario de entrada en el sidebar (lo dejamos igual)
st.sidebar.header("📋 Datos del Proyecto")
with st.sidebar.form("project_form"):
    direccion = st.text_input("Dirección del proyecto")
    precio_compra = st.number_input("Precio de compra", min_value=0.0, step=1000.0)
    arv = st.number_input("ARV (After Repair Value)", min_value=0.0, step=1000.0)
    renovacion = st.number_input("Costo de renovación", min_value=0.0, step=1000.0)
    comision = st.slider("Comisión de venta (%)", 0, 10, 5)
    tasa_prestamo = st.slider("Tasa préstamo anual (%)", 0, 20, 12)
    porcentaje_financiado = st.slider("% Financiado por lender", 0, 100, 70)
    tasa_gap = st.slider("Tasa preferente GAP (%)", 0, 20, 10)
    meses = st.slider("Tiempo estimado de ejecución (meses)", 1, 24, 6)
    renta = st.number_input("Renta mensual esperada", min_value=0.0, step=100.0)
    ocupacion = st.slider("Ocupación estimada (%)", 0, 100, 90)
    gastos_cierre = st.slider("Gastos de cierre (%)", 0, 10, 2)

    submitted = st.form_submit_button("Analizar proyecto")

# Procesamiento y resultados (igual)
if submitted:
    # Cálculos principales
    comision_total = arv * (comision / 100)
    financiado = precio_compra * (porcentaje_financiado / 100)
    gap = (precio_compra - financiado) + renovacion
    interes_prestamo = financiado * (tasa_prestamo / 100) * (meses / 12)
    interes_gap = gap * (tasa_gap / 100) * (meses / 12)
    gastos_cierre_val = precio_compra * (gastos_cierre / 100)


def crear_base_datos():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_base_datos()
    print("Base de datos y tabla de usuarios creadas correctamente.")
