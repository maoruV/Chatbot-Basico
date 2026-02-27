from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import streamlit as st

# Configuracion la pagina de la app
st.set_page_config(page_title="Chatbot Basico", page_icon="🤖")
st.title("🤖 Chatbot Basico con LangChain ")
st.markdown("Este es un chatbot basico contruido con langchain y streamlit. ¡Escribe tu mensaje y el chatbot responderá!")

with st.sidebar:
    st.header("Configuracion del Chatbot")
    st.info("Ajusta la temperatura y el modelo para personalizar las respuestas del chatbot.\n\nRecuerda que una temperatura más alta generará respuestas más creativas, mientras que una temperatura más baja hará que las respuestas sean más conservadoras.")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.5, 0.1)
    model_name = st.selectbox("Modelos", ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "openai/gpt-oss-120b", "openai/gpt-oss-20b"])

# Personalidad configurable
personalidad = st.selectbox(
    "Personalidad del asistente",
    [
        "Útil y amigable",
        "Profesional y formal", 
        "Casual y relajado",
        "Experto técnico",
        "Creativo y divertido"
    ]
)                          

# Configurar modelo
chat_model = ChatGroq(model=model_name, temperature=temperature)

# Definir los mensajes del sistema segun la personalidad
system_messages = {
    "Útil y amigable": "Eres un asistente útil y amigable llamado ChatBot Pro. Responde de manera clara y concisa.",
    "Profesional y formal": "Eres un asistente profesional y formal. Proporciona respuestas precisas y bien estructuradas.",
    "Casual y relajado": "Eres un asistente casual y relajado. Habla de forma natural y amigable, como un buen amigo.",
    "Experto técnico": "Eres un asistente experto técnico. Proporciona respuestas detalladas con precisión técnica.",
    "Creativo y divertido": "Eres un asistente creativo y divertido. Usa analogías, ejemplos creativos y mantén un tono alegre."
}

# ChatPromptTemplate con personalidad dinamica
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", system_messages[personalidad]),
    ("human", "Historial conversacion:\n{historial}\n\nPregunta actual: {mensaje}")
])


# Generar la respuesta usando LCEL (LangChain Expression Language) y el modelo de chat
cadena = chat_prompt | chat_model

# Inicializar el historial de mensajes
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# mostrar los mensajes previos en la interfaz
for msg in st.session_state.mensajes:
    if isinstance(msg, SystemMessage):
        #No muestro el mensaje por la interfaz
        continue
    
    role = "assistant" if isinstance(msg, AIMessage) else "user"
    with st.chat_message(role):
        st.markdown(msg.content)
        
if st.button("🗑️ Nueva Conversacion"):
    st.session_state.mensajes = []
    st.rerun()  # Reiniciar la aplicación para limpiar la interfaz
    
# entrada de texto del usuario Input para el usuario
pregunta = st.chat_input("Escribe tu mensaje: ")

if pregunta:
    # Mostrar el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(pregunta)
    
    # Preparar historial como texto
    historial_texto =""
    for msg in st.session_state.mensajes[-10:]: # Ultimos 10 mensajes
        if isinstance(msg, HumanMessage):
            historial_texto += f"usuario: {msg.content}\n"
        elif isinstance(msg, AIMessage):
            historial_texto += f"Asistente: {msg.content}\n"
            
    if not historial_texto:
        historial_texto ="(No hay historial previo)"
        
    # Generar y mostrar la respuesta del modelo en tiempo real usando streaming
    try:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()  # Placeholder para mostrar la respuesta del modelo en tiempo real
            full_response = ""  # Variable para acumular la respuesta completa del modelo
                
            # Uso el streaming del modelo para mostrar la respuesta en tiempo real
            for chunk in cadena.stream({"mensaje": pregunta, "historial": st.session_state.mensajes}):
                    full_response += chunk.content  # Acumulo la respuesta del modelo
                    response_placeholder.markdown(full_response + "▌")  # Actualizo el placeholder con la respuesta parcial y un cursor de carga
            response_placeholder.markdown(full_response)  # Finalmente, muestro la respuesta completa sin el cursor de carga
            
            # agreggo el mensaje del usuario en la memoria de streamlit
        st.session_state.mensajes.append(HumanMessage(content=pregunta))
        st.session_state.mensajes.append(AIMessage(content=full_response))
        
    except Exception as e:
        # Manejo de errores al generar la respuesta del modelo
        st.error(f"Error al generar respuesta: {str(e)}")
        st.info("Verifica que tu API Key esté configurada correctamente.")
            
        
    
    
    

    
    