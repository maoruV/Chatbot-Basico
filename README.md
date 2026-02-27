🤖 ChatBotMVG: Asistente Inteligente con LangChain & Streamlit
Este proyecto es una aplicación de chat interactiva que utiliza LangChain para la orquestación de modelos de lenguaje (LLM), Groq como motor de inferencia de alta velocidad y Streamlit para la interfaz de usuario.

✨ Características
Inferencia Ultra-rápida: Gracias a la integración con Groq.

Memoria de Contexto: El chatbot recuerda el historial de la conversación actual para dar respuestas coherentes.

Streaming de Respuestas: Los mensajes se muestran en tiempo real mientras se generan.

Configuración Dinámica: Permite ajustar el modelo y la temperatura (creatividad) desde la barra lateral.

Interfaz Limpia: Diseño basado en los componentes nativos de chat de Streamlit.

🛠️ Requisitos Previos
Antes de comenzar, asegúrate de tener una API Key de Groq Cloud.

🚀 Instalación y Uso (Recomendado con uv)
Para este proyecto, recomendamos usar uv, un administrador de paquetes de Python extremadamente rápido escrito en Rust.

1. Instalar uv
Si no tienes uv instalado, puedes hacerlo con un solo comando:

macOS/Linux:

Bash
curl -LsSf https://astral.sh/uv/install.sh | sh
Windows (PowerShell):

PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
2. Clonar el repositorio
Bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
3. Crear entorno virtual e instalar dependencias
Con uv, puedes crear el entorno y sincronizar todos los requisitos del archivo requirements.txt (o instalarlos directamente) de forma casi instantánea:

Bash
# Crea el entorno e instala todo lo necesario
uv venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
4. Configurar variables de entorno
Debes exportar tu clave de API de Groq en tu terminal:

Bash
# Linux/macOS
export GROQ_API_KEY="tu_api_key_aquí"

# Windows (Command Prompt)
set GROQ_API_KEY="tu_api_key_aquí"
💻 Ejecución
Para lanzar la aplicación, simplemente ejecuta:

Bash
streamlit run app.py
La aplicación se abrirá automáticamente en tu navegador, generalmente en http://localhost:8501.

🧠 Estructura del Código
LangChain Expression Language (LCEL): Se utiliza el operador pipe (|) para unir el prompt con el modelo de chat de forma declarativa.

Streamlit Session State: Se emplea st.session_state.mensajes para persistir el historial de la charla entre recargas de la página.

Streaming: Implementado mediante cadena.stream() para mejorar la experiencia de usuario (UX).

📄 Licencia
Este proyecto está bajo la licencia MIT.