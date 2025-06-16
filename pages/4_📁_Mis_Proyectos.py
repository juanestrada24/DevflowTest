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

# --- Mostrar fichas de proyectos en una sola columna ---
for proyecto in proyectos:
    with st.container():
        st.markdown(
            f"""
            <div style='
                border-radius: 10px;
                background: #F4F4F4;
                box-shadow: 0 2px 8px rgba(0,0,0,0.06);
                padding: 1.5rem 1.5rem 1rem 1.5rem;
                margin-bottom: 1.5rem;
                border: 2px solid #FF6B35;
            '>
                <h3 style='color:#0A1F44'>{proyecto["Proyecto"]}</h3>
                <ul style='padding-left:1.2em; color:#0A1F44;'>
                    <li><b>Tipo:</b> {proyecto["Tipo"]}</li>
                    <li><b>Ciudad:</b> {proyecto["Ciudad"]}</li>
                    <li><b>Estado:</b> {proyecto["Estado"]}</li>
                    <li><b>Inversión Total:</b> ${proyecto["Inversión Total"]:,.0f}</li>
                    <li><b>Avance Presupuestal:</b> {proyecto["Avance Presupuestal"]}%</li>
                </ul>
                <div style='background:#FF6B35;height:18px;border-radius:6px;width:{proyecto["Avance Presupuestal"]}%;max-width:100%;margin-bottom:0.5rem;'></div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")
st.markdown("Haz clic en un proyecto para ver su ficha completa de avance y análisis financiero. (Próximamente)")

# --- Vista de tabla breve ---
with st.expander("📋 Ver tabla resumen"):
    st.dataframe(df.style.format({"Inversión Total": "${:,.0f}", "Avance Presupuestal": "{:.0f}%"}))

# --- Gráfico de barras de avance presupuestal ---
st.subheader("Estado de Proyecto")

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
