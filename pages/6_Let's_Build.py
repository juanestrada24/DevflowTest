import streamlit as st

st.set_page_config(page_title="Conversacional Flip", layout="wide")
st.title("Flip conversacional 🤖")

campos = [
    {"key": "precio_compra", "label": "Precio de compra", "type": float, "value": 500000.0},
    {"key": "arv", "label": "ARV (valor tras renovación)", "type": float, "value": 700000.0},
    {"key": "renovacion", "label": "Costo de renovación", "type": float, "value": 50000.0},
    {"key": "comision", "label": "Comisión de venta (%)", "type": float, "value": 5.0},
    {"key": "tasa_prestamo", "label": "Tasa préstamo anual (%)", "type": float, "value": 12.0},
    {"key": "porcentaje_financiado", "label": "Porcentaje financiado por lender", "type": float, "value": 70.0},
    {"key": "tasa_gap", "label": "Tasa preferente del GAP investor (%)", "type": float, "value": 10.0},
    {"key": "meses", "label": "Duración del proyecto (meses)", "type": int, "value": 4},
    {"key": "renta_mensual", "label": "Renta mensual esperada", "type": float, "value": 0.0},
    {"key": "ocupacion", "label": "Ocupación estimada (%)", "type": float, "value": 0.0},
    {"key": "gastos_cierre", "label": "Gastos de cierre (%)", "type": float, "value": 1.5},
]

# Mostrar instrucciones y formato esperado
st.write("Por favor, ingresa todos los valores separados por coma, en el mismo orden que se muestra a continuación:")
for idx, campo in enumerate(campos):
    st.write(f"{idx+1}. **{campo['label']}** (ejemplo: {campo['value']})")

ejemplo = ", ".join(str(campo["value"]) for campo in campos)
st.info(f"Ejemplo: {ejemplo}")

if "conv_flip_data" not in st.session_state:
    st.session_state.conv_flip_data = {}
if "conv_flip_done" not in st.session_state:
    st.session_state.conv_flip_done = False

# Solo pide los datos si aún no se ingresaron correctamente
if not st.session_state.conv_flip_done:
    user_input = st.text_area(
        "Pega o escribe los valores separados por coma",
        value="",
        key="multi_campo_input",
        placeholder=ejemplo
    )
    if st.button("Enviar datos"):
        valores = [v.strip() for v in user_input.split(",")]
        if len(valores) != len(campos):
            st.error(f"Debes ingresar exactamente {len(campos)} valores, separados por coma.")
        else:
            datos = {}
            errores = []
            for idx, campo in enumerate(campos):
                try:
                    valor = campo["type"](valores[idx])
                    datos[campo["key"]] = valor
                except Exception:
                    errores.append(f"{campo['label']} ('{valores[idx]}')")

            if errores:
                st.error(f"Revisa estos campos: {', '.join(errores)}. Asegúrate de que sean del tipo correcto (número entero o decimal).")
            else:
                st.session_state.conv_flip_data = datos
                st.session_state.conv_flip_done = True
                st.success("¡Datos ingresados exitosamente!")
                st.rerun()
else:
    st.success("¡Datos ingresados exitosamente!")
    st.write("Resumen de tus respuestas:")
    st.json(st.session_state.conv_flip_data)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Enviar datos y continuar"):
            st.session_state["inputs"] = st.session_state.conv_flip_data
            st.session_state.conv_flip_data = {}
            st.session_state.conv_flip_done = False
            st.switch_page("pages/2_📊_Ficha_Analisis.py")
    with col2:
        if st.button("Volver a empezar"):
            st.session_state.conv_flip_data = {}
            st.session_state.conv_flip_done = False
            st.rerun()
