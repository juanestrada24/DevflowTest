# pages/4_🛠️_Distressed_Asset_Analysis.py

import streamlit as st

st.set_page_config(page_title="Análisis Distressed Asset", layout="wide")

st.title("🛠️ Análisis de Proyecto: Distressed Asset")

with st.form("form_distress"):
    st.subheader("1. Identificación del Proyecto")
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Nombre del proyecto")
        direccion = st.text_input("Dirección del activo")
        tipo_activo = st.selectbox("Tipo de activo", ["Multifamily", "Retail", "Office", "Industrial", "Hospitality", "Mixed-use"])
    with col2:
        estado = st.selectbox("Estado actual", ["Performing", "Non-performing", "En ejecución", "Subasta", "Off-market"])
        fuente = st.selectbox("Fuente del deal", ["Broker", "Banco", "Subasta", "Scraper", "Directo", "Otro"])
        contacto = st.text_input("Contacto del originador")

    st.markdown("---")

    st.subheader("2. Datos Financieros Actuales")
    col1, col2, col3 = st.columns(3)
    with col1:
        precio_adq = st.number_input("Precio de adquisición ($)", min_value=0.0, format="%.2f")
        valor_mercado = st.number_input("Valor mercado actual ($)", min_value=0.0, format="%.2f")
        arv = st.number_input("ARV estimado ($)", min_value=0.0, format="%.2f")
    with col2:
        renta_actual = st.number_input("Ingresos actuales ($/mes)", min_value=0.0, format="%.2f")
        gastos_actuales = st.number_input("Gastos operativos actuales ($/mes)", min_value=0.0, format="%.2f")
        deuda_mensual = st.number_input("Pago mensual deuda actual ($)", min_value=0.0, format="%.2f")
    with col3:
        noi_actual = renta_actual - gastos_actuales
        dscr_actual = (noi_actual * 12) / (deuda_mensual * 12) if deuda_mensual > 0 else 0
        st.metric("NOI actual (anual)", f"${noi_actual * 12:,.2f}")
        st.metric("DSCR actual", f"{dscr_actual:.2f}")

    st.markdown("---")

    st.subheader("3. Estrategia de Mejora")
    col1, col2, col3 = st.columns(3)
    with col1:
        capex = st.number_input("Costo de reposición (CapEx) ($)", min_value=0.0, format="%.2f")
        tiempo_mejora = st.number_input("Tiempo estimado de mejora (meses)", min_value=0)
    with col2:
        incremento_renta = st.number_input("Incremento estimado en renta (%)", min_value=0.0, format="%.2f")
        nueva_renta = renta_actual * (1 + incremento_renta / 100)
        nueva_vacancia = st.slider("Vacancia proyectada (%)", 0, 100, 10)
    with col3:
        nuevos_ingresos = nueva_renta * ((100 - nueva_vacancia) / 100)
        nuevos_gastos = st.number_input("Nuevos gastos operativos ($/mes)", min_value=0.0, format="%.2f")
        noi_proy = (nuevos_ingresos - nuevos_gastos) * 12
        dscr_proy = noi_proy / (deuda_mensual * 12) if deuda_mensual > 0 else 0
        st.metric("NOI proyectado (anual)", f"${noi_proy:,.2f}")
        st.metric("DSCR proyectado", f"{dscr_proy:.2f}")

    st.markdown("---")

    st.subheader("4. Estructura Financiera")
    col1, col2, col3 = st.columns(3)
    with col1:
        deuda_pct = st.slider("% Deuda senior", 0, 100, 70)
        tasa_deuda = st.number_input("Tasa deuda senior (%)", min_value=0.0, format="%.2f")
        plazo_deuda = st.number_input("Plazo deuda (meses)", min_value=0)
    with col2:
        gap_pct = st.slider("% GAP funding", 0, 100, 25)
        tasa_gap = st.number_input("Tasa preferente GAP (%)", min_value=0.0, format="%.2f")
        sponsor_pct = st.slider("% Equity sponsor", 0, 100, 5)
    with col3:
        honorarios = st.number_input("Honorarios Sponsor ($)", min_value=0.0, format="%.2f")
        comision_origen = st.number_input("Comisión de originación (%)", min_value=0.0, format="%.2f")

    st.markdown("---")

    st.subheader("5. Plan de Salida y KPIs")
    col1, col2, col3 = st.columns(3)
    with col1:
        estrategia_salida = st.selectbox("Estrategia de salida", ["Venta", "Refinanciación", "Retención con cashflow"])
        gastos_salida_pct = st.number_input("Gastos de salida (% ARV)", min_value=0.0, format="%.2f")
    with col2:
        meses_salida = st.number_input("Tiempo hasta salida (meses)", min_value=0)
        arv_final = arv
        gastos_salida = arv_final * (gastos_salida_pct / 100)
        ganancia_bruta = arv_final - precio_adq - capex - gastos_salida
    with col3:
        st.metric("Ganancia bruta estimada", f"${ganancia_bruta:,.2f}")
        split_inversionista = st.slider("Split Inversionista (%)", 0, 100, 70)
        split_sponsor = 100 - split_inversionista

    st.form_submit_button("Guardar análisis")

    st.success("✅ Análisis completo. Puedes guardar este proyecto o compartirlo.")
