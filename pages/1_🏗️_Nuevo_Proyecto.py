# Página: Nuevo Proyecto (Underwriting)
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Nuevo Proyecto", layout="wide")

# --- ESTILO DARK UI CORPORATIVO ---
st.markdown(
    """
    <style>
        body {
            background-color: #0A1626 !important;
        }
        .block-container {
            padding: 2rem 4rem;
            background-color: #0A1626;
            color: #F4F7FA;
            border-radius: 12px;
        }
        .stTextInput input, .stNumberInput input {
            background-color: #14233A;
            color: #F4F7FA;
            border-radius: 6px;
            border: 1.5px solid #2A4066;
            font-size: 16px;
        }
        .stNumberInput label, .stTextInput label {
            color: #F4F7FA;
            font-weight: 600;
        }
        .stButton>button {
            background-color: #1251A0;
            color: #F4F7FA;
            border: none;
            padding: 12px 28px;
            border-radius: 8px;
            font-size: 17px;
            font-weight: 600;
            transition: background 0.3s;
        }
        .stButton>button:hover {
            background-color: #1877D2;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: #F4F7FA;
        }
        .stForm {
            background: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Nuevo Proyecto")
st.markdown("Ingresa los datos clave para evaluar la oportunidad de inversión.")

with st.form("form_proyecto"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        direccion = st.text_input("Dirección de la propiedad")
        precio_compra = st.number_input("Precio de compra", min_value=0.0, step=1000.0, format="%.2f")
        costo_renovacion = st.number_input("Costo de renovación", min_value=0.0, step=1000.0, format="%.2f")
        comision_venta = st.number_input("Comisión de venta (%)", min_value=0.0, max_value=10.0, step=0.1)

    with col2:
        arv = st.number_input("ARV (Valor estimado post-renovación)", min_value=0.0, step=1000.0, format="%.2f")
        tasa_prestamo = st.number_input("Tasa préstamo anual (%)", min_value=0.0, step=0.5)
        porcentaje_financiado = st.number_input("% Financiado por lender", min_value=0.0, max_value=100.0, step=1.0)
        gastos_cierre = st.number_input("Gastos de cierre (%)", min_value=0.0, max_value=10.0, step=0.1)

    with col3:
        tasa_gap = st.number_input("Tasa preferente GAP (%)", min_value=0.0, max_value=20.0, step=0.5)
        meses = st.number_input("Tiempo de ejecución (meses)", min_value=1, step=1)
        renta_esperada = st.number_input("Renta mensual esperada", min_value=0.0, step=100.0)
        ocupacion = st.number_input("Ocupación estimada (%)", min_value=0.0, max_value=100.0, step=1.0)

    evaluar = st.form_submit_button("Evaluar Oportunidad")

    if evaluar:
        st.success("Datos recibidos. Dirígete a la pestaña 'Ficha de Análisis' para ver los resultados.")
