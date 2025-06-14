# DevFlow App - Página Principal
import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="DevFlow - Análisis de Proyecto",
    page_icon="🌐",
    layout="wide"
)

# CSS personalizado para estilos visuales, fondo azul oscuro y títulos centrados
st.markdown("""
    <style>
        .stApp {
            background: #182848;  /* Azul oscuro */
        }
        .main-title {
            text-align: center;
            color: #ffffff;
            font-size: 3rem;
            margin-bottom: 0.5em;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            color: #bcdff1;
            font-size: 1.5rem;
            margin-bottom: 2em;
        }
        /* NO ocultar el menú lateral para que aparezcan las páginas */
    </style>
""", unsafe_allow_html=True)

# Título principal y subtítulo con estilos
st.markdown('<div class="main-title">DevFlow</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Moviliza tus recursos con inteligencia</div>', unsafe_allow_html=True)

# Formulario de entrada
st.sidebar.header("📋 Datos del Proyecto")
with st.sidebar.form("project_form"):
    direccion = st.text_input("Dirección del proyecto")
    precio_compra = st.number_input("Precio de compra", min_value=0.0, step=1000.0)
    arv = st.number_input("ARV (After Repair Value)", min_value=0.0, step=1000.0)
    renovacion = st.number_input("Costo de renovación", min_value=0.0, step=1000.0)
    comision = st.slider("Comisión de venta (%)", 0, 10, 5)
    tasa_prestamo = st.slider("Tasa préstamo anual (%)", 0, 20, 12)
    porcentaje_financiado = st.slider("% Financiado por lender", 0, 100, 70)
    tasa_gap = st.slider("Tasa preferente GAP (%)", 0, 20, 10)
    meses = st.slider("Tiempo estimado de ejecución (meses)", 1, 24, 6)
    renta = st.number_input("Renta mensual esperada", min_value=0.0, step=100.0)
    ocupacion = st.slider("Ocupación estimada (%)", 0, 100, 90)
    gastos_cierre = st.slider("Gastos de cierre (%)", 0, 10, 2)

    submitted = st.form_submit_button("Analizar proyecto")

# Procesamiento y resultados
if submitted:
    # Cálculos principales
    comision_total = arv * (comision / 100)
    financiado = precio_compra * (porcentaje_financiado / 100)
    gap = (precio_compra - financiado) + renovacion
    interes_prestamo = financiado * (tasa_prestamo / 100) * (meses / 12)
    interes_gap = gap * (tasa_gap / 100) * (meses / 12)
    gastos_cierre_val = precio_compra * (gastos_cierre / 100)
    total_inversion = precio_compra + renovacion + comision_total + interes_prestamo + interes_gap + gastos_cierre_val
    upside = arv - total_inversion
    roi = (upside / gap) * 100 if gap > 0 else 0
    roi_anual = roi * (12 / meses) if meses > 0 else 0
    equity_multiple = (upside + gap) / gap if gap > 0 else 0

    # Métricas básicas en encabezado
    st.markdown(
        f"""
        <div style="font-size:0.95em; color: #bcdff1; margin-bottom: 0.7em; text-align:center;">
        <b>Dirección:</b> {direccion if direccion else "-"} &nbsp; | &nbsp;
        <b>Precio de compra:</b> ${precio_compra:,.0f} &nbsp; | &nbsp;
        <b>Costo de renovación:</b> ${renovacion:,.0f} &nbsp; | &nbsp;
        <b>ARV:</b> ${arv:,.0f} &nbsp; | &nbsp;
        <b>ROI inversionista:</b> {roi:.1f}% &nbsp; | &nbsp;
        <b>ROI anualizado:</b> {roi_anual:.1f}% &nbsp; | &nbsp;
        <b>Equity Multiple:</b> {equity_multiple:.2f} &nbsp; | &nbsp;
        <b>Tiempo de ejecución:</b> {meses} meses
        </div>
        <hr>
        """, unsafe_allow_html=True
    )

    # Métricas principales
    col1, col2 = st.columns(2)
    with col1:
        st.metric("ARV", f"${arv:,.0f}")
        st.metric("Costo Total", f"${total_inversion:,.0f}")
        st.metric("Upside", f"${upside:,.0f}")
        st.metric("ROI", f"{roi:.1f}%")
    with col2:
        st.metric("Interés Préstamo", f"${interes_prestamo:,.0f}")
        st.metric("Interés GAP", f"${interes_gap:,.0f}")
        st.metric("ROI Anualizado", f"{roi_anual:.1f}%")
        st.metric("Equity Multiple", f"{equity_multiple:.2f}")

    # Estado de resultados (tabla breakdown)
    breakdown_data = {
        "Concepto": [
            "Precio de compra",
            "Costo de renovación",
            "Comisión de venta",
            "Interés préstamo",
            "Interés GAP",
            "Gastos de cierre",
            "Total inversión",
            "ARV",
            "Upside (ganancia)"
        ],
        "Monto": [
            precio_compra,
            renovacion,
            comision_total,
            interes_prestamo,
            interes_gap,
            gastos_cierre_val,
            total_inversion,
            arv,
            upside
        ]
    }
    df_breakdown = pd.DataFrame(breakdown_data)
    df_breakdown["Monto"] = df_breakdown["Monto"].apply(lambda x: f"${x:,.0f}")
    st.markdown("### Estado de resultados del ejercicio")
    st.table(df_breakdown)

    st.success("✅ Análisis generado con éxito.")
    st.info("En próximas versiones podrás compartir este análisis con aliados o exportar como PDF.")
