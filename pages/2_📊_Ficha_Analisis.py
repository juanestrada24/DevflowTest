# Página: Ficha de Análisis
import streamlit as st

st.set_page_config(page_title="Ficha de Análisis", layout="wide")

# --- Validación de inputs ---
if "inputs" not in st.session_state:
    st.error("⚠️ No se han ingresado datos. Por favor, complete el formulario en 'Nuevo Proyecto'.")
    st.stop()

# --- Cargar datos del formulario ---
data = st.session_state["inputs"]
precio_compra = data["precio_compra"]
arv = data["arv"]
renovacion = data["renovacion"]
comision = data["comision"]
tasa_prestamo = data["tasa_prestamo"]
porcentaje_financiado = data["porcentaje_financiado"]
tasa_gap = data["tasa_gap"]
meses = data["meses"]
renta_mensual = data["renta_mensual"]
ocupacion = data["ocupacion"]
gastos_cierre = data["gastos_cierre"]

# --- Cálculos ---
comision_venta = arv * (comision / 100)
monto_prestamo = precio_compra * (porcentaje_financiado / 100)
downpayment = precio_compra - monto_prestamo
gap_inversion = downpayment + renovacion
interes_prestamo = monto_prestamo * (tasa_prestamo / 100) * (meses / 12)
interes_gap = gap_inversion * (tasa_gap / 100) * (meses / 12)
cierre = precio_compra * (gastos_cierre / 100)
total_costos = precio_compra + renovacion + comision_venta + interes_prestamo + interes_gap + cierre
upside = arv - total_costos

# ROI Proyecto
roi_proyecto = upside / total_costos
# ROI Inversionista
roi_inversionista = (interes_gap + (upside / 2)) / gap_inversion
equity_multiple = 1 + roi_inversionista

# --- Estilos dark UI ---
st.markdown(
    """
    <style>
        .block-container {
            background-color: #0B1C2C;
            color: #FFFFFF;
        }
        .card {
            background-color: #1C2F40;
            border-radius: 8px;
            padding: 1.5rem;
            text-align: center;
            border: 1px solid #35526F;
        }
        .metric-label {
            font-size: 14px;
            color: #AAAAAA;
        }
        .metric-value {
            font-size: 28px;
            font-weight: bold;
        }
        .table-style td {
            padding: 8px 16px;
            border-bottom: 1px solid #3A4A5F;
        }
        .stButton>button {
            background-color: #007FFF;
            color: white;
            font-weight: bold;
            padding: 0.6rem 1.2rem;
            border-radius: 5px;
            margin-right: 10px;
        }
        .stButton>button:hover {
            background-color: #00A4FF;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- KPIs Principales ---
st.title("📊 Ficha de Inversión")

col1, col2, col3 = st.columns(3)
col1.markdown(f'<div class="card"><div class="metric-label">Valor de Compra</div><div class="metric-value">${precio_compra:,.0f}</div></div>', unsafe_allow_html=True)
col2.markdown(f'<div class="card"><div class="metric-label">ARV</div><div class="metric-value">${arv:,.0f}</div></div>', unsafe_allow_html=True)
col3.markdown(f'<div class="card"><div class="metric-label">Duración</div><div class="metric-value">{meses} meses</div></div>', unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)
col4.markdown(f'<div class="card"><div class="metric-label">ROI Inversionista</div><div class="metric-value">{roi_inversionista:.1%}</div></div>', unsafe_allow_html=True)
col5.markdown(f'<div class="card"><div class="metric-label">ROI Proyecto</div><div class="metric-value">{roi_proyecto:.1%}</div></div>', unsafe_allow_html=True)
col6.markdown(f'<div class="card"><div class="metric-label">Equity Multiple</div><div class="metric-value">{equity_multiple:.2f}x</div></div>', unsafe_allow_html=True)

st.markdown("---")

# --- Tabla tipo estado de resultados ---
st.subheader("🧾 Estado Financiero del Proyecto")
st.markdown(f"""
<table class="table-style">
<tr><td>ARV (valor de reventa)</td><td>${arv:,.0f}</td></tr>
<tr><td>Precio de compra</td><td>${precio_compra:,.0f}</td></tr>
<tr><td>Costo de renovación</td><td>${renovacion:,.0f}</td></tr>
<tr><td>Comisión de venta ({comision}%)</td><td>${comision_venta:,.0f}</td></tr>
<tr><td>Intereses préstamo</td><td>${interes_prestamo:,.0f}</td></tr>
<tr><td>Intereses GAP</td><td>${interes_gap:,.0f}</td></tr>
<tr><td>Gastos de cierre ({gastos_cierre}%)</td><td>${cierre:,.0f}</td></tr>
<tr><td><strong>Upside (ganancia neta)</strong></td><td><strong>${upside:,.0f}</strong></td></tr>
</table>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Botones de acción ---
col_a, col_b = st.columns([1, 1])
col_a.button("📤 Compartir oportunidad")
col_b.button("🤝 Invitar colegas")
