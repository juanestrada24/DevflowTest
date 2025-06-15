# Página: Ficha de Análisis
# Página: Ficha de Análisis
import streamlit as st

# --- Configuración de página ---
st.set_page_config(page_title="Ficha de Análisis", layout="wide")

# --- Estilo DARK UI tipo Exchange ---
st.markdown(
    """
    <style>
        .block-container {
            background-color: #0B1C2C;
            color: #FFFFFF;
            padding: 2rem;
        }
        .card {
            background-color: #1C2F40;
            border-radius: 8px;
            padding: 1.5rem;
            text-align: center;
            color: #FFFFFF;
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

# --- Título ---
st.title("📊 Ficha de Inversión")
st.markdown("Análisis financiero del proyecto.")

# --- KPIs principales (hardcoded) ---
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="card"><div class="metric-label">Valor de Compra</div><div class="metric-value">$525,000</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><div class="metric-label">ARV</div><div class="metric-value">$750,000</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="card"><div class="metric-label">Duración</div><div class="metric-value">3 meses</div></div>', unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)
with col4:
    st.markdown('<div class="card"><div class="metric-label">ROI Inversionista</div><div class="metric-value">30.5%</div></div>', unsafe_allow_html=True)
with col5:
    st.markdown('<div class="card"><div class="metric-label">ROI Proyecto</div><div class="metric-value">43.6%</div></div>', unsafe_allow_html=True)
with col6:
    st.markdown('<div class="card"><div class="metric-label">Equity Multiple</div><div class="metric-value">1.30x</div></div>', unsafe_allow_html=True)

st.markdown("---")

# --- Estado de resultados (tabla simulada) ---
st.subheader("🧾 Estado Financiero del Proyecto")
st.markdown("""
<table class="table-style">
<tr><td>ARV (valor de reventa)</td><td>$750,000</td></tr>
<tr><td>Precio de compra</td><td>$525,000</td></tr>
<tr><td>Costo de renovación</td><td>$50,000</td></tr>
<tr><td>Comisión de venta (5%)</td><td>$37,500</td></tr>
<tr><td>Intereses préstamo (3 meses a 12%)</td><td>$11,025</td></tr>
<tr><td>Intereses GAP (3 meses a 10%)</td><td>$3,862</td></tr>
<tr><td>Gastos de cierre (1.5%)</td><td>$7,875</td></tr>
<tr><td><strong>Upside (ganancia neta)</strong></td><td><strong>$115,738</strong></td></tr>
</table>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Botones de acción ---
col_a, col_b = st.columns([1, 1])
with col_a:
    st.button("📤 Compartir oportunidad")
with col_b:
    st.button("🤝 Invitar colegas")
