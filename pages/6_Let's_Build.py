# pages/6_let’s_build.py

import streamlit as st
import openai

# --- Configuración de la página ---
st.set_page_config(page_title="Let’s Build – Análisis Conversacional", layout="wide")

# --- Clave API desde secrets ---
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- Título ---
st.title("🏗️ Let’s Build")
st.subheader("Describe tu operación inmobiliaria en lenguaje natural y analizamos los KPIs del flip.")

# --- Input del usuario ---
user_input = st.text_area(
    "✍️ Describe tu flip inmobiliario (compra, renovación, ARV, tiempo, etc.):",
    placeholder="Ej: Estoy comprando una casa por $350,000, planeo renovarla por $45,000 y venderla por $520,000. Tomará 6 meses...",
    height=180
)

# --- Botón de análisis ---
if st.button("🔍 Analizar Flip"):
    if not user_input.strip():
        st.warning("Por favor ingresa una descripción para analizar.")
    else:
        with st.spinner("Procesando análisis..."):

            # --- Prompt a OpenAI ---
            prompt = f"""
Eres un analista financiero de flips inmobiliarios. A partir de la siguiente descripción, extrae los siguientes campos:

- precio_compra (USD)
- renovacion (USD)
- arv (USD)
- comision_venta (porcentaje, asume 6% si no se menciona)
- tiempo_proyecto (en meses, asume 6 si no se menciona)

Luego calcula:
- utilidad_bruta = arv - (precio_compra + renovacion + comision_venta)
- ROI = utilidad_bruta / (precio_compra + renovacion)
- equity_multiple = arv / (precio_compra + renovacion)

Devuelve un diccionario de Python como este ejemplo:
{{
  "precio_compra": 350000,
  "renovacion": 45000,
  "arv": 520000,
  "comision_venta": 31200,
  "tiempo_proyecto_meses": 6,
  "utilidad_bruta": 93800,
  "ROI": 0.22,
  "equity_multiple": 1.22
}}

Descripción:
\"\"\"{user_input}\"\"\"
"""

            # --- Llamada a OpenAI ---
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2
                )

                result = response["choices"][0]["message"]["content"]

                # --- Mostrar resultado ---
                st.success("✅ Análisis generado")
                st.code(result, language="python")

            except Exception as e:
                st.error(f"❌ Error al generar análisis: {str(e)}")
