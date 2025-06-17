# pages/6_let’s_build.py
# pages/6_let’s_build.py

import streamlit as st
from openai import OpenAI
import openai

# --- Configuración de la página ---
st.set_page_config(page_title="Let’s Build – Asistente de Flip", layout="wide")

# --- Inicializar cliente OpenAI con tu API Key desde secrets.toml ---
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except KeyError:
    st.error("❌ No se encontró la clave 'OPENAI_API_KEY'. Agrega tu API key en .streamlit/secrets.toml o en los secrets de Streamlit Cloud.")
    st.stop()

# --- Título e instrucciones ---
st.title("🏗️ Let’s Build")
st.subheader("Describe tu operación de flip y recibe KPIs automáticamente.")

st.markdown("""
Escribe en lenguaje natural los detalles de tu inversión inmobiliaria (compra, renovación, ARV, duración, comisión, etc.)  
y este asistente extraerá los valores clave y calculará los principales KPIs financieros como ROI, utilidad y múltiplo de equity.
""")

# --- Campo de entrada ---
user_input = st.text_area(
    "✍️ Describe tu operación de flip:",
    placeholder="Ej: Estoy comprando una casa por $385,000, renovándola con $45,000 y la vendo por $510,000 en 5 meses...",
    height=180
)

# --- Botón para analizar ---
if st.button("🔍 Analizar Flip"):
    if not user_input.strip():
        st.warning("Por favor ingresa una descripción.")
        st.stop()

    with st.spinner("Procesando..."):

        # --- Prompt para el asistente ---
        prompt = f"""
Eres un analista financiero especializado en flips inmobiliarios.

Del siguiente texto, extrae:
- precio_compra (en USD)
- renovacion (en USD)
- arv (en USD)
- comision_venta (en USD o porcentaje; si no se menciona, asume 6%)
- tiempo_proyecto (en meses; si no se menciona, asume 6)

Luego calcula:
- utilidad_bruta = arv - (precio_compra + renovacion + comision_venta)
- ROI = utilidad_bruta / (precio_compra + renovacion)
- equity_multiple = arv / (precio_compra + renovacion)

Devuelve un diccionario de Python como este ejemplo:
{{
  "precio_compra": 385000,
  "renovacion": 45000,
  "arv": 510000,
  "comision_venta": 30600,
  "tiempo_proyecto_meses": 5,
  "utilidad_bruta": 49600,
  "ROI": 0.114,
  "equity_multiple": 1.114
}}

Texto:
\"\"\"{user_input}\"\"\"
"""

        try:
            # --- Llamada a OpenAI ---
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # ✅ Compatible con todas las cuentas
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2
            )

            result = response.choices[0].message.content
            st.success("✅ Resultado generado")
            st.code(result, language="python")

        except openai.OpenAIError as e:
            st.error(f"❌ Error con la API: {e}")
        except Exception as e:
            st.error(f"❌ Error inesperado: {e}")
