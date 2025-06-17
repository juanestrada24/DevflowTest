import streamlit as st
import re

st.set_page_config(page_title="Conversacional Flip", layout="wide")
st.title("Flip conversacional 🤖")

# Definición de campos y si son requeridos para KPIs básicos
campos = [
    {"key": "precio_compra", "label": "Precio de compra", "type": float, "value": 500000.0, "required": True},
    {"key": "arv", "label": "ARV (valor tras renovación)", "type": float, "value": 700000.0, "required": True},
    {"key": "renovacion", "label": "Costo de renovación", "type": float, "value": 50000.0, "required": True},
    {"key": "comision", "label": "Comisión de venta (%)", "type": float, "value": 5.0, "required": False},
    {"key": "tasa_prestamo", "label": "Tasa préstamo anual (%)", "type": float, "value": 12.0, "required": False},
    {"key": "porcentaje_financiado", "label": "Porcentaje financiado por lender", "type": float, "value": 70.0, "required": False},
    {"key": "tasa_gap", "label": "Tasa preferente del GAP investor (%)", "type": float, "value": 10.0, "required": False},
    {"key": "meses", "label": "Duración del proyecto (meses)", "type": int, "value": 4, "required": False},
    {"key": "renta_mensual", "label": "Renta mensual esperada", "type": float, "value": 0.0, "required": False},
    {"key": "ocupacion", "label": "Ocupación estimada (%)", "type": float, "value": 0.0, "required": False},
    {"key": "gastos_cierre", "label": "Gastos de cierre (%)", "type": float, "value": 1.5, "required": False},
]
campo_por_key = {c["key"]: c for c in campos}

# Estado conversacional
if "conv_flip_data" not in st.session_state:
    st.session_state.conv_flip_data = {}
if "conv_flip_faltantes" not in st.session_state:
    st.session_state.conv_flip_faltantes = []
if "conv_flip_done" not in st.session_state:
    st.session_state.conv_flip_done = False
if "conv_flip_chat" not in st.session_state:
    st.session_state.conv_flip_chat = []

def mostrar_chat():
    for entrada in st.session_state.conv_flip_chat:
        st.chat_message(entrada["role"]).write(entrada["content"])

def procesar_entrada(texto):
    # Buscar pares campo=valor
    entradas = re.findall(r"(\w+)\s*=\s*([0-9\.\-]+)", texto)
    nuevos_datos = {}
    errores = []
    for key, valor in entradas:
        key = key.lower()
        if key in campo_por_key:
            try:
                tipo = campo_por_key[key]["type"]
                nuevos_datos[key] = tipo(valor)
            except Exception:
                errores.append(key)
        else:
            errores.append(key)
    return nuevos_datos, errores

def calcular_kpis(datos):
    # Solo calcula los KPIs que pueda con los datos disponibles
    resultados = {}

    # KPI 1: Ganancia bruta = ARV - (precio_compra + renovacion)
    if all(k in datos for k in ["arv", "precio_compra", "renovacion"]):
        resultados["Ganancia Bruta"] = datos["arv"] - (datos["precio_compra"] + datos["renovacion"])
    
    # KPI 2: ROI simple = Ganancia bruta / precio_compra
    if "Ganancia Bruta" in resultados and "precio_compra" in datos and datos["precio_compra"] != 0:
        resultados["ROI Simple (%)"] = 100 * resultados["Ganancia Bruta"] / datos["precio_compra"]

    # KPI 3: Comisión de venta (si existe)
    if all(k in datos for k in ["arv", "comision"]):
        resultados["Comisión de Venta"] = datos["arv"] * datos["comision"] / 100

    # KPI 4: Gastos de cierre (si existe)
    if all(k in datos for k in ["arv", "gastos_cierre"]):
        resultados["Gastos de Cierre"] = datos["arv"] * datos["gastos_cierre"] / 100

    # KPI 5: Renta bruta esperada (si existe)
    if all(k in datos for k in ["renta_mensual", "meses", "ocupacion"]):
        resultados["Renta Bruta Esperada"] = datos["renta_mensual"] * datos["meses"] * (datos["ocupacion"] / 100 if datos["ocupacion"] else 1)

    return resultados

if st.session_state.conv_flip_done:
    mostrar_chat()
    st.chat_message("assistant").success("¡Datos ingresados exitosamente! 🎉")
    st.chat_message("assistant").write("Resumen de tus respuestas:")
    st.chat_message("assistant").json(st.session_state.conv_flip_data)
    resultados = calcular_kpis(st.session_state.conv_flip_data)
    if resultados:
        st.chat_message("assistant").write("KPIs calculados con tus datos:")
        st.chat_message("assistant").json(resultados)
    else:
        st.chat_message("assistant").warning("No se pudo calcular ningún KPI con los datos actuales.")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Enviar datos y continuar"):
            st.session_state["inputs"] = st.session_state.conv_flip_data
            st.session_state.conv_flip_data = {}
            st.session_state.conv_flip_done = False
            st.session_state.conv_flip_chat = []
            st.session_state.conv_flip_faltantes = []
            st.switch_page("pages/2_📊_Ficha_Analisis.py")
    with col2:
        if st.button("Volver a empezar"):
            st.session_state.conv_flip_data = {}
            st.session_state.conv_flip_done = False
            st.session_state.conv_flip_chat = []
            st.session_state.conv_flip_faltantes = []
            st.rerun()
else:
    datos_actuales = st.session_state.conv_flip_data
    # Faltantes solo para los KPIs más básicos (ganancia bruta y ROI)
    faltantes_kpi_basico = [
        c for c in campos if c["required"] and c["key"] not in datos_actuales
    ]
    todos_faltantes = [
        c for c in campos if c["key"] not in datos_actuales
    ]

    mostrar_chat()

    # Mensaje inicial o por faltantes
    if not datos_actuales:
        pregunta = (
            "Por favor, ingresa los datos que conozcas en formato campo=valor, separados por coma. "
            "Por ejemplo: precio_compra=500000, renovacion=40000, meses=5. "
            "Puedes ingresar solo los que conozcas, los KPIs se calcularán con los datos disponibles."
        )
        st.session_state.conv_flip_chat.append({"role": "assistant", "content": pregunta})
    elif todos_faltantes:
        resumen = "Datos recibidos hasta ahora:\n"
        for k, v in datos_actuales.items():
            resumen += f"- **{campo_por_key[k]['label']}**: {v}\n"
        resumen += "\nPuedes agregar más datos (opcional) para ver KPIs más detallados:\n"
        for c in todos_faltantes:
            ejemplo = f"{c['key']}={c['value']}"
            resumen += f"- **{c['label']}** (ejemplo: {ejemplo})\n"
        st.session_state.conv_flip_chat.append({"role": "assistant", "content": resumen})

    # Mostrar KPIs parciales si se puede calcular alguno
    resultados = calcular_kpis(datos_actuales)
    if resultados:
        st.chat_message("assistant").write("KPIs calculados hasta ahora:")
        st.chat_message("assistant").json(resultados)

    user_input = st.chat_input("Escribe aquí tus datos en formato campo=valor...")

    if user_input is not None:
        st.session_state.conv_flip_chat.append({"role": "user", "content": user_input})
        nuevos_datos, errores = procesar_entrada(user_input)
        if nuevos_datos:
            st.session_state.conv_flip_data.update(nuevos_datos)
        if errores:
            error_msg = "No pude reconocer o convertir estos campos: " + ", ".join(errores)
            st.session_state.conv_flip_chat.append({"role": "assistant", "content": error_msg})

        # Si ya tenemos todos los requeridos para los KPIs básicos, damos opción de terminar,
        # pero permitimos seguir agregando datos opcionales para KPIs adicionales.
        datos_actuales = st.session_state.conv_flip_data
        faltantes_kpi_basico = [c for c in campos if c["required"] and c["key"] not in datos_actuales]
        if not faltantes_kpi_basico:
            st.session_state.conv_flip_done = True
        st.rerun()
