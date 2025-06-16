# Página: Historial del Usuario

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Colores de DevFlow
COLOR_BARRA = "#FF6B35"
COLOR_TEXTO = "#0A1F44"
COLOR_FONDO = "#F4F4F4"

# Configuración de página
st.set_page_config(page_title="Mis Proyectos", layout="wide")

st.title("📁 Mis Proyectos")
st.markdown("Resumen general de tus inversiones activas con indicadores clave y progreso de ejecución.")

# --- Datos simulados (puedes conectar luego con tu base de datos o estado) ---
proyectos = [
    {
        "Proyecto": "7th Ave Townhomes",
        "Tipo": "Obra nueva",
        "Ciudad": "Miami",
        "Estado": "En construcción",
        "Inversión Total": 950000,
        "Avance Presupuestal": 65
    },
    {
        "Proyecto": "Coral Gables Flip",
        "Tipo": "Flip",
        "Ciudad": "Coral Gables",
        "Estado": "Comercialización",
        "Inversión Total": 450000,
        "Avance Presupuestal": 95
    },
    {
        "Proyecto": "West Palm Warehouse",
        "Tipo": "Distressed",
        "Ciudad": "West Palm Beach",
        "Estado": "Adquisición",
        "Inversión Total": 1250000,
        "Avance Presupuestal": 15
    }
]

df = pd.DataFrame(proyectos)

# --- Vista de tabla breve ---
with st.expander("📋 Ver tabla resumen"):
    st.dataframe(df.style.format({"Inversión Total": "${:,.0f}", "Avance Presupuestal": "{:.0f}%"}))

# --- Gráfico de barras de avance presupuestal ---
st.subheader("📊 Avance de Presupuesto por Proyecto")

fig, ax = plt.subplots(figsize=(10, 4))
bars = ax.barh(df["Proyecto"], df["Avance Presupuestal"], color=COLOR_BARRA)

ax.set_xlabel("Avance Presupuestal (%)", color=COLOR_TEXTO)
ax.set_xlim(0, 100)
ax.set_title("Progreso de Ejecución por Proyecto", fontsize=14, color=COLOR_TEXTO)
ax.xaxis.set_major_formatter(ticker.PercentFormatter())

# Etiquetas sobre barras
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2,
            f'{width:.0f}%', va='center', color=COLOR_TEXTO, fontsize=10)

ax.tick_params(axis='y', colors=COLOR_TEXTO)
ax.tick_params(axis='x', colors=COLOR_TEXTO)
fig.patch.set_facecolor(COLOR_FONDO)
ax.set_facecolor("white")

st.pyplot(fig)

# --- Placeholder para vincular con vistas detalladas ---
st.markdown("---")
st.markdown("Haz clic en un proyecto para ver su ficha completa de avance y análisis financiero. (Próximamente)")
