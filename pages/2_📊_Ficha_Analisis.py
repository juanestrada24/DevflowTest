# Página: Ficha de Análisis
import streamlit as st

st.set_page_config(page_title="Ficha de Análisis", layout="wide")

# --- Validación de inputs ---
if "inputs" not in st.session_state:
    st.error("⚠️ No se han ingresado datos. Por favor, complete el formulario en 'New Flip'.")
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

# --- Estilos dark UI y botones customizados ---
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
        /* Botón azul neutro Devflow */
        .stButton > button {
            background-color: #263238 !important;  /* Azul más neutro, acorde a Devflow */
            color: #FFFFFF !important;
            font-weight: bold;
            padding: 0.6rem 1.2rem;
            border-radius: 5px;
            margin-right: 10px;
            border: none;
            transition: background 0.2s;
        }
        .stButton > button:hover {
            background-color: #0000FF !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- KPIs Principales en grid de 3 columnas con fuente más pequeña y ROI en verde limón ---
st.title("Project Data Sheet")

st.markdown(
    """
    <style>
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
            margin-bottom: 32px;
        }}
        .kpi-card {{
            background-color: #1C2F40;
            border-radius: 8px;
            padding: 1.2rem 0.8rem;
            text-align: center;
            border: 1px solid #35526F;
        }}
        .kpi-label {{
            font-size: 12px;
            color: #AAAAAA;
            margin-bottom: 4px;
        }}
        .kpi-value {{
            font-size: 22px;
            font-weight: bold;
            margin-top: 2px;
        }}
        .kpi-lime {{
            color: #BFFF00;
        }}
    </style>
    <div class="kpi-grid">
        <div class="kpi-card">
            <div class="kpi-label">Valor de Compra</div>
            <div class="kpi-value">${:,.0f}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">ARV</div>
            <div class="kpi-value">${:,.0f}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Duración</div>
            <div class="kpi-value">{} meses</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">ROI Inversionista</div>
            <div class="kpi-value kpi-lime">{:.1%}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">ROI Proyecto</div>
            <div class="kpi-value kpi-lime">{:.1%}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Equity Multiple</div>
            <div class="kpi-value">{:.2f}x</div>
        </div>
    </div>
    """.format(
        precio_compra,
        arv,
        meses,
        roi_inversionista,
        roi_proyecto,
        equity_multiple
    ),
    unsafe_allow_html=True)

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

# --- Valores de texto adicionales debajo de la tabla ---
asking_price_sqft = precio_compra / 1500  # Suponiendo 1500 sqft (ajústalo según tu contexto)
arv_sqft = arv / 1500
lot_size_sqft = 5000  # puedes traerlo como campo adicional luego
units = 1             # idem
beds = 3              # idem

st.markdown(
    f"""
    <div style="font-size: 14px; color: #AAAAAA; margin-top: -10px; margin-bottom: 25px;">
        <strong>Asking price/sqft:</strong> ${asking_price_sqft:,.2f} &nbsp;|&nbsp;
        <strong>ARV/sqft:</strong> ${arv_sqft:,.2f} &nbsp;|&nbsp;
        <strong>Lot size:</strong> {lot_size_sqft:,} sqft &nbsp;|&nbsp;
        <strong>Units:</strong> {units} &nbsp;|&nbsp;
        <strong>Beds:</strong> {beds}
    </div>
    """,
    unsafe_allow_html=True
)
# --- NUEVA TABLA DE INDICADORES DE OPERACIÓN ---

# 1. CAP Rate
if renta_mensual > 0 and ocupacion > 0:
    cap_rate = (renta_mensual * 12 * (ocupacion / 100)) / (precio_compra + renovacion)
else:
    cap_rate = None

# 2. Spread
if arv > 0 and total_costos > 0:
    spread = (arv - total_costos) / arv
else:
    spread = None

# 3. DSCR
interes_prestamo_anual = monto_prestamo * (tasa_prestamo / 100)
if renta_mensual > 0 and monto_prestamo > 0 and interes_prestamo_anual > 0 and ocupacion > 0:
    dscr = (renta_mensual * 12 * (ocupacion / 100)) / interes_prestamo_anual
else:
    dscr = None

# 4. Velocidad de absorción del barrio (sin dato)
absorcion = None

st.subheader("📈 Indicadores de Operación")

st.markdown(f"""
<table class="table-style">
<tr>
    <td>CAP Rate (si se alquila)</td>
    <td>{f"{cap_rate:.2%}" if cap_rate is not None else ""}</td>
</tr>
<tr>
    <td>Spread (margen entre ARV y costos totales)</td>
    <td>{f"{spread:.2%}" if spread is not None else ""}</td>
</tr>
<tr>
    <td>DSCR</td>
    <td>{f"{dscr:.2f}" if dscr is not None else ""}</td>
</tr>
<tr>
    <td>Velocidad de absorción del barrio</td>
    <td></td>
</tr>
</table>
""", unsafe_allow_html=True)

# --- Botones de acción ---
col_a, col_b = st.columns([2, 2])

with col_a:
    st.button("📤 Share")
    st.button("📑 Add to pipeline")

with col_b:
    st.button("🤝 Invite colleages")
    st.button("📞 Schedule call")
