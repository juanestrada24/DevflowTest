# Página: Nuevo Proyecto (Underwriting)
import streamlit as st

st.set_page_config(page_title="New Flip", layout="wide")
st.title("New Flip")  # o el texto que uses como título principal

# --- ESTILO: ANCHO MÓVIL ---
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
        /* ---- ESTILOS EXTRA PARA MOBILE ---- */
        @media (max-width: 800px) {
            .block-container {
                padding-left: 0.5rem !important;
                padding-right: 0.5rem !important;
                max-width: 100vw !important;
            }
            .stTextInput input, .stNumberInput input {
                min-width: 92vw !important;
                max-width: 98vw !important;
                font-size: 18px !important;
                padding: 14px !important;
            }
            .stButton>button {
                min-width: 90vw !important;
                max-width: 98vw !important;
                font-size: 19px !important;
                padding: 16px 0 !important;
            }
            .stNumberInput, .stTextInput, .stForm {
                width: 100% !important;
            }
            label {
                font-size: 17px !important;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("Ingresa los datos clave para evaluar la oportunidad de inversión.")

with st.form(key="form_nuevo_proyecto"):
    st.subheader("Datos del Proyecto")
    col1, col2, col3 = st.columns(3)

    with col1:
        precio_compra = st.number_input("Precio de compra", min_value=0.0, value=500000.0, step=1000.0, format="%.2f")
        renovacion = st.number_input("Costo de renovación", min_value=0.0, value=50000.0, step=1000.0, format="%.2f")
        arv = st.number_input("ARV (valor tras renovación)", min_value=0.0, value=700000.0, step=1000.0, format="%.2f")
        meses = st.number_input("Duración del proyecto (meses)", min_value=1, value=4, step=1)
        
    with col2:
        
        porcentaje_financiado = st.number_input("% Financiado por lender", min_value=0.0, max_value=100.0, value=70.0, step=1.0)
        tasa_prestamo = st.number_input("Tasa préstamo anual (%)", min_value=0.0, value=12.0, step=0.5)
        comision = st.number_input("Comisión de venta (%)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
        gastos_cierre = st.number_input("Gastos de cierre (%)", min_value=0.0, max_value=10.0, value=1.5, step=0.1)

    with col3:
        downpayment = st.number_input("Downpayment", min_value=0.0, value=0.0, step=1000.0, format="%.2f")
        tasa_gap = st.number_input("Tasa preferente del GAP investor (%)", min_value=0.0, max_value=20.0, value=10.0, step=0.5)
        renta_mensual = st.number_input("Renta mensual esperada", min_value=0.0, value=0.0, step=100.0)
        ocupacion = st.number_input("Ocupación estimada (%)", min_value=0.0, max_value=100.0, value=0.0, step=1.0)

    submit = st.form_submit_button("Check Deal")

if submit:
    # Guardar datos en session_state
    st.session_state["inputs"] = {
        "precio_compra": precio_compra,
        "arv": arv,
        "renovacion": renovacion,
        "comision": comision,
        "tasa_prestamo": tasa_prestamo,
        "porcentaje_financiado": porcentaje_financiado,
        "tasa_gap": tasa_gap,
        "meses": meses,
        "renta_mensual": renta_mensual,
        "ocupacion": ocupacion,
        "gastos_cierre": gastos_cierre
    }
    # Redirigir automáticamente a la página de análisis
    st.switch_page("pages/2_📊_Ficha_Analisis.py")
