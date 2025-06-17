import streamlit as st

st.set_page_config(page_title="Conversacional Flip", layout="wide")
st.title("Flip conversacional 🤖")

# Configuración de los campos y sus tipos
campos = [
    {"key": "precio_compra", "label": "¿Cuál es el precio de compra?", "type": float, "value": 500000.0},
    {"key": "arv", "label": "¿Cuál es el ARV (valor tras renovación)?", "type": float, "value": 700000.0},
    {"key": "renovacion", "label": "¿Cuál es el costo de renovación?", "type": float, "value": 50000.0},
    {"key": "comision", "label": "¿Cuál es la comisión de venta (%)?", "type": float, "value": 5.0},
    {"key": "tasa_prestamo", "label": "¿Cuál es la tasa préstamo anual (%)?", "type": float, "value": 12.0},
    {"key": "porcentaje_financiado", "label": "¿Qué porcentaje es financiado por lender?", "type": float, "value": 70.0},
    {"key": "tasa_gap", "label": "¿Cuál es la tasa preferente del GAP investor (%)?", "type": float, "value": 10.0},
    {"key": "meses", "label": "¿Cuál es la duración del proyecto (meses)?", "type": int, "value": 4},
    {"key": "renta_mensual", "label": "¿Cuál es la renta mensual esperada?", "type": float, "value": 0.0},
    {"key": "ocupacion", "label": "¿Cuál es la ocupación estimada (%)?", "type": float, "value": 0.0},
    {"key": "gastos_cierre", "label": "¿Cuáles son los gastos de cierre (%)?", "type": float, "value": 1.5},
]

# Estados de la conversación y respuestas
if "conv_flip_i" not in st.session_state:
    st.session_state.conv_flip_i = 0
if "conv_flip_data" not in st.session_state:
    st.session_state.conv_flip_data = {}
if "conv_flip_chat" not in st.session_state:
    st.session_state.conv_flip_chat = []

i = st.session_state.conv_flip_i

# Función para mostrar el historial de chat
def mostrar_chat():
    for entrada in st.session_state.conv_flip_chat:
        st.chat_message(entrada["role"]).write(entrada["content"])

# Lógica conversacional tipo chat
if i < len(campos):
    campo = campos[i]
    # Mensaje del sistema (pregunta)
    if len(st.session_state.conv_flip_chat) == 0 or st.session_state.conv_flip_chat[-1]["role"] == "user":
        st.session_state.conv_flip_chat.append({"role": "assistant", "content": campo["label"]})
    mostrar_chat()
    user_input = st.chat_input("Escribe tu respuesta y presiona Enter...")

    if user_input is not None:
        # Agrega la respuesta del usuario al chat
        st.session_state.conv_flip_chat.append({"role": "user", "content": user_input})
        # Valida el tipo de dato
        try:
            if campo['type'] == int:
                respuesta = int(user_input)
            else:
                respuesta = float(user_input)
            st.session_state.conv_flip_data[campo["key"]] = respuesta
            st.session_state.conv_flip_i += 1
            st.rerun()
        except Exception:
            st.session_state.conv_flip_chat.append(
                {"role": "assistant", "content": "❗ Por favor ingresa un valor numérico válido."}
            )
            st.rerun()
else:
    # Mostrar historial y resumen final
    mostrar_chat()
    st.chat_message("assistant").success("¡Datos ingresados exitosamente! 🎉")
    st.chat_message("assistant").write("Resumen de tus respuestas:")
    st.chat_message("assistant").json(st.session_state.conv_flip_data)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Enviar datos y continuar"):
            st.session_state["inputs"] = st.session_state.conv_flip_data
            st.session_state.conv_flip_i = 0
            st.session_state.conv_flip_data = {}
            st.session_state.conv_flip_chat = []
            st.switch_page("pages/2_📊_Ficha_Analisis.py")
    with col2:
        if st.button("Volver a empezar"):
            st.session_state.conv_flip_i = 0
            st.session_state.conv_flip_data = {}
            st.session_state.conv_flip_chat = []
            st.rerun()
