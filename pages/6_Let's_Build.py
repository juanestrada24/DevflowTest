import streamlit as st

st.set_page_config(page_title="Conversacional Flip", layout="wide")
st.title("Flip conversacional 🤖")

# Lista ordenada de los campos a solicitar
campos = [
    {"key": "precio_compra", "label": "¿Cuál es el precio de compra?", "type": "number", "min": 0.0, "value": 500000.0, "step": 1000.0, "format": "%.2f"},
    {"key": "arv", "label": "¿Cuál es el ARV (valor tras renovación)?", "type": "number", "min": 0.0, "value": 700000.0, "step": 1000.0, "format": "%.2f"},
    {"key": "renovacion", "label": "¿Cuál es el costo de renovación?", "type": "number", "min": 0.0, "value": 50000.0, "step": 1000.0, "format": "%.2f"},
    {"key": "comision", "label": "¿Cuál es la comisión de venta (%)?", "type": "number", "min": 0.0, "max": 10.0, "value": 5.0, "step": 0.1},
    {"key": "tasa_prestamo", "label": "¿Cuál es la tasa préstamo anual (%)?", "type": "number", "min": 0.0, "value": 12.0, "step": 0.5},
    {"key": "porcentaje_financiado", "label": "¿Qué porcentaje es financiado por lender?", "type": "number", "min": 0.0, "max": 100.0, "value": 70.0, "step": 1.0},
    {"key": "tasa_gap", "label": "¿Cuál es la tasa preferente del GAP investor (%)?", "type": "number", "min": 0.0, "max": 20.0, "value": 10.0, "step": 0.5},
    {"key": "meses", "label": "¿Cuál es la duración del proyecto (meses)?", "type": "number", "min": 1, "value": 4, "step": 1},
    {"key": "renta_mensual", "label": "¿Cuál es la renta mensual esperada?", "type": "number", "min": 0.0, "value": 0.0, "step": 100.0},
    {"key": "ocupacion", "label": "¿Cuál es la ocupación estimada (%)?", "type": "number", "min": 0.0, "max": 100.0, "value": 0.0, "step": 1.0},
    {"key": "gastos_cierre", "label": "¿Cuáles son los gastos de cierre (%)?", "type": "number", "min": 0.0, "max": 10.0, "value": 1.5, "step": 0.1},
]

# Estado conversacional: en qué campo vamos
if "conv_flip_ongoing" not in st.session_state:
    st.session_state.conv_flip_ongoing = True
if "conv_flip_i" not in st.session_state:
    st.session_state.conv_flip_i = 0
if "conv_flip_data" not in st.session_state:
    st.session_state.conv_flip_data = {}

# Mostrar preguntas y guardar respuesta
i = st.session_state.conv_flip_i
if st.session_state.conv_flip_ongoing and i < len(campos):
    campo = campos[i]
    respuesta = st.number_input(
        campo["label"],
        min_value=campo.get("min"),
        max_value=campo.get("max"),
        value=campo.get("value"),
        step=campo.get("step"),
        format=campo.get("format") if "format" in campo else None,
        key=f"input_{campo['key']}_{i}"
    )
    if st.button("Siguiente"):
        st.session_state.conv_flip_data[campo["key"]] = respuesta
        st.session_state.conv_flip_i += 1
        st.experimental_rerun()
elif st.session_state.conv_flip_ongoing:
    st.success("¡Datos ingresados exitosamente!")
    st.write("Resumen de tus respuestas:")
    st.json(st.session_state.conv_flip_data)
    if st.button("Enviar datos y continuar"):
        st.session_state["inputs"] = st.session_state.conv_flip_data
        st.session_state.conv_flip_ongoing = False
        st.switch_page("pages/2_📊_Ficha_Analisis.py")
    if st.button("Volver a empezar"):
        st.session_state.conv_flip_i = 0
        st.session_state.conv_flip_data = {}
        st.experimental_rerun()
else:
    st.success("¡Flujo completado!")
    if st.button("Reiniciar"):
        st.session_state.conv_flip_ongoing = True
        st.session_state.conv_flip_i = 0
        st.session_state.conv_flip_data = {}
        st.experimental_rerun()
