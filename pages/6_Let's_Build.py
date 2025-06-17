# app.py

import streamlit as st
import openai

# --- Configuración inicial ---
st.set_page_config(page_title="Análisis Conversacional de Flips", layout="wide")

# --- Clave de API (cargarla desde secrets o entorno) ---
openai.api_key = st.secrets["OPENAI_API_KEY"]  # asegúrate de tenerla en .streamlit/secrets.toml

# --- Título de la app ---
st.title("Análisis Conversacional de un Flip")

# --- Campo de texto conversacional ---
user_input = st.text_area("Describe tu operación inmobiliaria:", height=150)

# --- Botón para procesar ---
if st.button("Analizar"):
    if not user_input:
        st.warning("Por favor ingresa una descripción.")
    else:
        with st.spinner("Procesando..."):

            prompt = f"""
Extrae los siguientes campos desde esta descripción de texto sobre una inversión de flipping inmobiliario:
- precio_compra
- renovacion
- arv
- comision_venta (porcentaje si se menciona)
- tiempo_proyecto (en meses si se menciona)

Luego calcula:
- ROI
- upside
- equity_multiple

Descripción:
\"\"\"{user_input}\"\"\"

Devuelve solo un diccionario de Python con los valores numéricos calculados y extraídos.
"""

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )

            result = response["choices"][0]["message"]["content"]
            st.code(result, language="python")
