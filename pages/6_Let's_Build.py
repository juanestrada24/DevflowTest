# pages/6_let’s_build.py
# pages/6_let’s_build.py

import streamlit as st
import openai
from openai import OpenAI

# --- Configurar la página ---
st.set_page_config(page_title="Let’s Build – Asistente de Flip", layout="wide")

# --- Inicializar cliente OpenAI ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- Título y descripción ---
st.title("🏗️ Let’s Build")
st.subheader("Habla con el asistente y recibe KPIs de tu operación inmobiliaria")

st.markdown("""
Escribe en lenguaje natural detalles de tu flip inmobiliario (precio de compra, renovación, ARV, duración, comisión, etc.)  
y deja que el asistente extraiga los valores clave y calcule ROI, upside, equity multiple y más.
""")

# --- Input de usuario ---
user_input = st.text_area(
    "✍️ Describe tu operación de flip:",
    placeholder="Ej: Estoy comprando una casa por $385,000, renovándola con $45,000 y la vendo por $510,000 en 5 meses...",
    height=180
)

# --- Procesamiento al hacer clic ---
if st.button("🔍 Analizar"):
    if not user_input.strip():
        st.warning("Por favor ingresa una descripción.")
    else:
        with st.spinner("Procesando..."):

            prompt = f"""
Eres un asistente experto en inversiones inmobiliarias tipo flipping.

Del siguiente texto, extrae:
- precio_compra
- renovacion
- arv
- comision_venta (% o asume 6%)
- tiempo_proyecto en meses (si no se menciona, asume 6)

Luego calcula:
- utilidad_bruta = arv - (precio_compra + renovacion + comision_venta)
- ROI = utilidad_bruta / (precio_compra + renovacion)
- equity_multiple = arv / (precio_compra + renovacion)

Muestra todos los resultados como un diccionario de Python.

Texto:
\"\"\"{user_input}\"\"\"
"""

            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2
                )

                result = response.choices[0].message.content
                st.success("✅ Resultado generado")
                st.code(result, language="python")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
