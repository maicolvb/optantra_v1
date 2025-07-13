import streamlit as st
import openai
import os
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Page configuration
st.set_page_config(
    page_title="Optantra IA - Diagnóstico Logístico Inteligente",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .suggestion-box {
        background: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🧠 Optantra IA</h1>
    <h3>Diagnóstico Logístico Inteligente con IA</h3>
</div>
""", unsafe_allow_html=True)

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuración")
    
    # API Key input with better validation
    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Ingresa tu clave de API de OpenAI (debe empezar con 'sk-')",
        value=os.getenv("OPENAI_API_KEY", ""),
        placeholder="sk-..."
    )
    
    # API Key validation
    if api_key:
        if not api_key.startswith("sk-"):
            st.error("❌ La clave API debe empezar con 'sk-'")
        else:
            openai.api_key = api_key
            st.success("✅ Clave API configurada")
    else:
        st.warning("⚠️ Ingresa tu clave de API de OpenAI")
    
    # Help section
    with st.expander("🔧 ¿Cómo obtener mi clave API?"):
        st.markdown("""
        1. Ve a [OpenAI Platform](https://platform.openai.com/api-keys)
        2. Crea una cuenta o inicia sesión
        3. Haz clic en "Create new secret key"
        4. Copia la clave (empieza con `sk-`)
        5. Pégala aquí o en un archivo `.env`
        """)
    
    st.markdown("---")
    st.markdown("### 📊 Métricas del Sistema")
    
    # Mock metrics (in a real app, these would come from your database)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Problemas Resueltos", "127")
        st.metric("Tiempo Promedio", "2.3 días")
    with col2:
        st.metric("Eficiencia", "89%")
        st.metric("Ahorro Estimado", "$45K")

# Main content
procesos = [
    "Recibo y entrada de mercancía",
    "Control y planeación del inventario", 
    "Compras y gestión de proveedores",
    "Alistamiento y despacho de pedidos",
    "Gestión de almacenes",
    "Transporte y distribución",
    "Gestión de devoluciones",
    "Análisis de datos y reportes"
]

# Create two columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔍 Diagnóstico del Problema")
    
    # Process selection
    proceso_elegido = st.selectbox(
        "Selecciona el proceso que presenta problemas:",
        procesos,
        help="Elige el área logística donde necesitas asistencia"
    )
    
    # Problem description
    descripcion = st.text_area(
        "Describe el problema en detalle:",
        placeholder="Ej: Tenemos retrasos constantes en la entrega de productos, los clientes se quejan de demoras de 3-5 días...",
        height=120
    )
    
    # Urgency level
    urgencia = st.select_slider(
        "Nivel de urgencia:",
        options=["Baja", "Media", "Alta", "Crítica"],
        value="Media"
    )
    
    # Additional context
    contexto_adicional = st.text_area(
        "Contexto adicional (opcional):",
        placeholder="Información sobre el tamaño de la empresa, industria, ubicación, etc.",
        height=80
    )

with col2:
    st.subheader("📋 Información Adicional")
    
    # Company size
    tamano_empresa = st.selectbox(
        "Tamaño de la empresa:",
        ["Pequeña (1-50 empleados)", "Mediana (51-200 empleados)", "Grande (200+ empleados)"]
    )
    
    # Industry
    industria = st.selectbox(
        "Industria:",
        ["Retail", "Manufactura", "E-commerce", "Alimentación", "Textil", "Otros"]
    )
    
    # Budget consideration
    presupuesto = st.selectbox(
        "Consideración de presupuesto:",
        ["Bajo", "Medio", "Alto", "Sin restricción"]
    )

# Generate AI suggestion
if st.button("🚀 Generar Diagnóstico Inteligente", type="primary"):
    if not api_key:
        st.error("⚠️ Por favor, ingresa tu clave de API de OpenAI en la barra lateral.")
    elif not descripcion.strip():
        st.error("⚠️ Por favor, describe el problema para generar sugerencias.")
    else:
        with st.spinner("🤖 Analizando con IA..."):
            try:
                # Prepare the prompt for ChatGPT
                prompt = f"""
                Eres un experto consultor en logística y cadena de suministros con más de 15 años de experiencia.
                
                Analiza el siguiente problema logístico y proporciona:
                1. Un diagnóstico detallado del problema
                2. 3-5 soluciones específicas y accionables
                3. Una estimación de tiempo de implementación
                4. Beneficios esperados
                5. Riesgos potenciales
                
                Información del problema:
                - Proceso: {proceso_elegido}
                - Descripción: {descripcion}
                - Urgencia: {urgencia}
                - Contexto adicional: {contexto_adicional}
                - Tamaño empresa: {tamano_empresa}
                - Industria: {industria}
                - Presupuesto: {presupuesto}
                
                Responde en español de manera profesional pero accesible. Usa emojis para hacer la respuesta más visual.
                """
                
                # Call OpenAI API
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Eres un consultor experto en logística y cadena de suministros."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=1000,
                    temperature=0.7
                )
                
                ai_suggestion = response.choices[0].message.content
                
                # Display results
                st.success("✅ Análisis completado con éxito!")
                
                # Create tabs for better organization
                tab1, tab2, tab3 = st.tabs(["🤖 Diagnóstico IA", "📊 Métricas", "💡 Acciones Rápidas"])
                
                with tab1:
                    st.markdown(f"""
                    <div class="suggestion-box">
                        {ai_suggestion}
                    </div>
                    """, unsafe_allow_html=True)
                
                with tab2:
                    st.subheader("📈 Métricas de Impacto Estimado")
                    
                    # Mock impact metrics based on urgency
                    if urgencia in ["Alta", "Crítica"]:
                        impacto_tiempo = "15-30 días"
                        impacto_costo = "20-40% reducción"
                        impacto_eficiencia = "25-35% mejora"
                    else:
                        impacto_tiempo = "30-60 días"
                        impacto_costo = "10-25% reducción"
                        impacto_eficiencia = "15-25% mejora"
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("⏱️ Tiempo de Implementación", impacto_tiempo)
                    with col2:
                        st.metric("💰 Ahorro Estimado", impacto_costo)
                    with col3:
                        st.metric("📈 Mejora en Eficiencia", impacto_eficiencia)
                
                with tab3:
                    st.subheader("⚡ Acciones Inmediatas Recomendadas")
                    
                    # Quick actions based on process
                    quick_actions = {
                        "Recibo y entrada de mercancía": [
                            "🔍 Revisar procedimientos de inspección",
                            "📋 Implementar checklist digital",
                            "⏰ Establecer tiempos estándar"
                        ],
                        "Control y planeación del inventario": [
                            "📊 Realizar auditoría de inventario",
                            "🔄 Implementar sistema de rotación",
                            "📈 Análisis ABC de productos"
                        ],
                        "Compras y gestión de proveedores": [
                            "🤝 Evaluar proveedores actuales",
                            "📋 Renegociar términos de pago",
                            "📊 Implementar scorecard de proveedores"
                        ],
                        "Alistamiento y despacho de pedidos": [
                            "📦 Optimizar layout del almacén",
                            "⚡ Implementar picking por zonas",
                            "📱 Usar tecnología móvil"
                        ]
                    }
                    
                    actions = quick_actions.get(proceso_elegido, [
                        "📋 Documentar proceso actual",
                        "🔍 Identificar cuellos de botella",
                        "📊 Recolectar datos de rendimiento"
                    ])
                    
                    for action in actions:
                        st.markdown(f"• {action}")
                
            except Exception as e:
                st.error(f"❌ Error al conectar con la IA: {str(e)}")
                st.info("💡 Asegúrate de que tu clave de API sea válida y tengas créditos disponibles.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🧠 Powered by OpenAI GPT | 🚀 Desarrollado con Streamlit</p>
</div>
""", unsafe_allow_html=True)

