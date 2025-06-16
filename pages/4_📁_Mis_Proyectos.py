import streamlit as st
import pandas as pd

# Colores de DevFlow
COLOR_BARRA = "#FF6B35"
COLOR_TEXTO = "#0A1F44"
COLOR_FONDO = "#F4F4F4"

st.set_page_config(page_title="Mis Proyectos", layout="wide")

st.title("📁 Mis Proyectos")
st.markdown("Resumen general de tus inversiones activas con indicadores clave y progreso de ejecución.")

proyectos = [
    {
        "Proyecto": "Edificio Central",
        "Tipo": "Construcción",
        "Ciudad": "Bogotá",
        "Estado": "En progreso",
        "Inversión Total": 500000000,
        "Avance Presupuestal": 60,
    },
    {
        "Proyecto": "Parque Solar",
        "Tipo": "Energía",
        "Ciudad": "Medellín",
        "Estado": "Planificado",
        "Inversión Total": 300000000,
        "Avance Presupuestal": 20,
    },
    {
        "Proyecto": "Residencial Sur",
        "Tipo": "Vivienda",
        "Ciudad": "Cali",
        "Estado": "Terminado",
        "Inversión Total": 200000000,
        "Avance Presupuestal": 100,
    },
]

for proyecto in proyectos:
    with st.container():
        st.markdown(
            f"""
            <div style='
                border-radius: 10px;
                background: #F4F4F4;
                box-shadow: 0 2px 8px rgba(0,0,0,0.06);
                padding: 1.5rem 2.5rem 1rem 2.5rem;
                margin-bottom: 1.5rem;
              border: 2px solid #333333;
            '>
                <h3 style='color:#0A1F44'>{proyecto["Proyecto"]}</h3>
                <div style='color:#0A1F44; font-size:1.1rem; margin-bottom:0.5rem;'>
                    <b>Tipo:</b> {proyecto["Tipo"]} &nbsp;|&nbsp;
                    <b>Ciudad:</b> {proyecto["Ciudad"]} &nbsp;|&nbsp;
                    <b>Estado:</b> {proyecto["Estado"]} &nbsp;|&nbsp;
                    <b>Inversión Total:</b> ${proyecto["Inversión Total"]:,.0f} &nbsp;|&nbsp;
                    <b>Avance Presupuestal:</b> {proyecto["Avance Presupuestal"]}%
                </div>
                <div style='background:#FF6B35;height:18px;border-radius:6px;width:{proyecto["Avance Presupuestal"]}%;max-width:100%;margin-bottom:0.5rem;'></div>
            </div>
            """,
            unsafe_allow_html=True
        )
