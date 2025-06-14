# Página: Nuevo Proyecto (Underwriting)
import streamlit as st

st.set_page_config(page_title="Nuevo Proyecto", layout="wide")

# --- ESTILO GENERAL ---
st.markdown(
    """
    <style>
        .block-container {
            padding: 2rem 4rem;
            background-color: #f8f9fa;
        }
        .stTextInput > div > div > input {
            background-color: #ffffff;
            color: #000000;
        }
        .stNumberInput > div > input {
            background-color: #ffffff;
            color: #000000;
        }
        .stButton>button {
            background-color: #003366;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #0055aa;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏗️ Nuevo Proyecto")
st.markdown("Ingresa los datos clave para evaluar la oportunidad de inversión.")

with st.form("form_proyecto"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        direccion = st.text_input("📍 Dirección de la propiedad")
        precio_compra = st.number_input("💰 Precio de compra", min_value=0.0, step=1000.0, format="%.2f")
        costo_renovacion = st.number_input("🛠 Costo de renovación", min_value=0.0, step=1000.0, format="%.2f")
        comision_venta = st.number_input("💼 Comisión de venta (%)", min_value=0.0, max_value=10.0, step=0.1)

    with col2:
        arv = st.number_input("📈 ARV (Valor estimado post-renovación)", min_value=0.0, step=1000.0, format="%.2f")
        tasa_prestamo = st.number_input("🏦 Tasa préstamo anual (%)", min_value=0.0, step=0.5)
        porcentaje_financiado = st.number_input("🔧 % Financiado por lender", min_value=0.0, max_value=100.0, step=1.0)
        gastos_cierre = st.number_input("💸 Gastos de cierre (%)", min_value=0.0, max_value=10.0, step=0.1)

    with col3:
        tasa_gap = st.number_input("🔹 Tasa preferente GAP (%)", min_value=0.0, max_value=20.0, step=0.5)
        meses = st.number_input("📆 Tiempo de ejecución (meses)", min_value=1, step=1)
        renta_esperada = st.number_input("🏠 Renta mensual esperada (si aplica)", min_value=0.0, step=100.0)
        ocupacion = st.number_input("📊 Ocupación estimada (%)", min_value=0.0, max_value=100.0, step=1.0)

    evaluar = st.form_submit_button("📊 Evaluar Oportunidad")

    if evaluar:
        st.success("✅ Datos recibidos. Dirígete a la pestaña 'Ficha de Análisis' para ver los resultados.")
