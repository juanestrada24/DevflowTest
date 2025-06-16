import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Colores de DevFlow
COLOR_BARRA = "#003366"
COLOR_TEXTO = "#0A1F44"
COLOR_FONDO = "#F4F4F4"

# Configuración de página
st.set_page_config(page_title="Mis Proyectos", layout="wide")

st.title("📁 Mis Proyectos")
st.markdown("Resumen general de tus inversiones activas con indicadores clave y progreso de ejecución.")

# --- EJEMPLO: Lista de proyectos, reemplaza con tus datos reales o conéctalo a la base de datos ---
proyectos = [
    {
        "Proyecto": "145 SE 25TH RD. MIAMI, FL",
        "Tipo": "Flip",
        "Ciudad": "Miami",
        "Estado": "En obra",
        "Inversión Total": 500000000,
        "Avance Presupuestal": 60,
    },
    {
        "Proyecto": "New construction",
        "Tipo": "Brickell 25",
        "Ciudad": "Miami",
        "Estado": "Planificado",
        "Inversión Total": 300000000,
        "Avance Presupuestal": 20,
    },
    {
        "Proyecto": "1180 NW 24 ST",
        "Tipo": "Flip",
        "Ciudad": "Broward",
        "Estado": "Terminado",
        "Inversión Total": 200000000,
        "Avance Presupuestal": 100,
    },
    # Puedes agregar más proyectos aquí o cargar desde una base de datos
]

df = pd.DataFrame(proyectos)

# --- Mostrar fichas de proyectos en una sola columna con dos columnas internas para los textos ---
for proyecto in proyectos:
    with st.container():
        st.markdown(
            f"""
            <div style='
                border-radius: 10px;
                background: {COLOR_FONDO};
                box-shadow: 0 2px 8px rgba(0,0,0,0.06);
                padding: 0.75rem 1rem 0.5rem 1rem;
                margin-bottom: 1rem;
                border: 2px solid {COLOR_BARRA};
            '>
                <h3 style='color:{COLOR_TEXTO}'>{proyecto["Proyecto"]}</h3>
                <div style='display: flex; gap: 2rem;'>
                  <ul style='padding-left:1.2em; color:{COLOR_TEXTO}; flex: 1; list-style: none; margin: 0;'>
                      <li><b>Tipo:</b> {proyecto["Tipo"]}</li>
                      <li><b>Ciudad:</b> {proyecto["Ciudad"]}</li>
                  </ul>
                  <ul style='padding-left:1.2em; color:{COLOR_TEXTO}; flex: 1; list-style: none; margin: 0;'>
                      <li><b>Estado:</b> {proyecto["Estado"]}</li>
                      <li><b>Inversión Total:</b> ${proyecto["Inversión Total"]:,.0f}</li>
                      <li><b>Avance Presupuestal:</b> {proyecto["Avance Presupuestal"]}%</li>
                  </ul>
                </div>
                <div style='background:{COLOR_BARRA};height:14px;border-radius:6px;width:{proyecto["Avance Presupuestal"]}%;max-width:100%;margin-bottom:0.5rem;'></div>
            </div>
            """,
            unsafe_allow_html=True
        )
