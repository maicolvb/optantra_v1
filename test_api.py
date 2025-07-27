# optantra_customs.py - Tu app existente + Claude para análisis aduanero

import streamlit as st
import anthropic
from datetime import datetime
import json
import pandas as pd
from PIL import Image
import pytesseract
import PyPDF2
import io

# Configuración de página (mantén tu estilo)
st.set_page_config(
    page_title="Optantra IA - Análisis Aduanero",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilo personalizado (tu branding morado)
st.markdown("""
<style>
    .main {
        background-color: #1a1a2e;
    }
    .stButton>button {
        background-color: #7c3aed;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #6d28d9;
        transform: scale(1.05);
    }
    .success-box {
        background-color: #10b981;
        padding: 1rem;
        border-radius: 10px;
        color: white;
    }
    .error-box {
        background-color: #ef4444;
        padding: 1rem;
        border-radius: 10px;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar Claude
@st.cache_resource
def init_claude():
    """Inicializa Claude con manejo de errores"""
    try:
        # Primero intenta con la clave de Streamlit secrets
        if "ANTHROPIC_API_KEY" in st.secrets:
            return anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
        else:
            st.error("⚠️ Configura tu ANTHROPIC_API_KEY en Streamlit Secrets")
            st.info("Ve a Settings → Secrets en tu app de Streamlit Cloud")
            return None
    except Exception as e:
        st.error(f"Error al inicializar Claude: {str(e)}")
        return None

# Header con tu branding
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style='text-align: center; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 20px; margin-bottom: 2rem;'>
        <h1 style='color: white; margin: 0;'>🧠 Optantra IA</h1>
        <h3 style='color: white; margin: 0;'>Análisis Aduanero Inteligente con Claude</h3>
    </div>
    """, unsafe_allow_html=True)

# Sidebar mejorado
with st.sidebar:
    st.markdown("### ⚙️ Configuración")
    
    # Selector de idioma
    language = st.selectbox(
        "Idioma / Language",
        ["Español", "English"],
        index=0
    )
    
    # Tipo de análisis
    analysis_type = st.selectbox(
        "Tipo de Análisis",
        ["Completo", "Rápido", "Cumplimiento", "Clasificación Arancelaria"]
    )
    
    st.markdown("---")
    st.markdown("### 📊 Métricas del Sistema")
    
    # Métricas (puedes conectar a tu DB)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Documentos Hoy", "12", "+3")
    with col2:
        st.metric("Precisión", "94%", "+2%")

# Inicializar Claude
claude_client = init_claude()

# Tabs principales
tab1, tab2, tab3, tab4 = st.tabs(["📤 Análisis", "📊 Dashboard", "📜 Historial", "🔧 Configuración"])

with tab1:
    st.markdown("### Análisis de Documentos Aduaneros")
    
    # Área de carga mejorada
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Arrastra tu documento aquí o haz clic para seleccionar",
            type=['pdf', 'png', 'jpg', 'jpeg'],
            help="Soportamos facturas comerciales, BL, declaraciones aduaneras"
        )
        
        if uploaded_file:
            # Preview del documento
            if uploaded_file.type == "application/pdf":
                st.success(f"✅ PDF cargado: {uploaded_file.name}")
            else:
                image = Image.open(uploaded_file)
                st.image(image, caption="Vista previa del documento", use_column_width=True)
    
    with col2:
        st.markdown("### Tipo de Documento")
        doc_type = st.radio(
            "Selecciona:",
            ["Factura Comercial", "Bill of Lading", "Declaración Aduanera", "Packing List", "Certificado Origen"],
            label_visibility="collapsed"
        )
        
        st.markdown("### Información Adicional")
        country_origin = st.selectbox("País Origen", ["México", "China", "USA", "Alemania", "Otro"])
        urgent = st.checkbox("⚡ Procesamiento Urgente")

    # Botón de análisis con estado
    if uploaded_file and claude_client:
        if st.button("🚀 Analizar con Claude", type="primary", use_container_width=True):
            
            # Progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Paso 1: Extraer texto
                status_text.text("📄 Extrayendo texto del documento...")
                progress_bar.progress(25)
                
                if uploaded_file.type == "application/pdf":
                    pdf_reader = PyPDF2.PdfReader(uploaded_file)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text()
                else:
                    image = Image.open(uploaded_file)
                    text = pytesseract.image_to_string(image, lang='spa+eng')
                
                # Paso 2: Preparar prompt
                status_text.text("🤖 Preparando análisis con Claude...")
                progress_bar.progress(50)
                
                prompt = f"""Eres un experto en comercio internacional y aduanas. Analiza este documento tipo {doc_type} y extrae la siguiente información en formato JSON:

                1. Información General:
                   - Número de documento
                   - Fecha
                   - Tipo de documento
                
                2. Partes Involucradas:
                   - Exportador (nombre, dirección, tax ID)
                   - Importador (nombre, dirección, tax ID)
                   - Notify party (si aplica)
                
                3. Mercancías:
                   - Descripción detallada
                   - Código HS/HTS (si está disponible)
                   - Cantidad
                   - Valor unitario
                   - Valor total
                
                4. Información Logística:
                   - País de origen
                   - País de destino
                   - Puerto de carga/descarga
                   - Incoterm
                
                5. Cumplimiento:
                   - Campos faltantes críticos
                   - Posibles errores
                   - Recomendaciones
                
                Documento:
                {text[:3000]}
                
                Responde SOLO con el JSON, sin explicaciones adicionales."""
                
                # Paso 3: Análisis con Claude
                status_text.text("🧠 Claude está analizando tu documento...")
                progress_bar.progress(75)
                
                response = claude_client.messages.create(
                    model="claude-3-sonnet-20240229",  # Más económico que Opus
                    max_tokens=2000,
                    messages=[{
                        "role": "user",
                        "content": prompt
                    }]
                )
                
                # Paso 4: Procesar resultados
                status_text.text("✨ Generando reporte...")
                progress_bar.progress(90)
                
                try:
                    result = json.loads(response.content[0].text)
                    
                    # Mostrar resultados en formato atractivo
                    st.markdown("---")
                    st.markdown("## 📋 Resultados del Análisis")
                    
                    # Información general
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.markdown("**📄 Documento**")
                        st.info(result.get('informacion_general', {}).get('numero_documento', 'N/A'))
                    with col2:
                        st.markdown("**📅 Fecha**")
                        st.info(result.get('informacion_general', {}).get('fecha', 'N/A'))
                    with col3:
                        st.markdown("**🏷️ Tipo**")
                        st.info(doc_type)
                    
                    # Partes involucradas
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("### 📤 Exportador")
                        exp = result.get('partes_involucradas', {}).get('exportador', {})
                        st.write(f"**Nombre:** {exp.get('nombre', 'N/A')}")
                        st.write(f"**Tax ID:** {exp.get('tax_id', 'N/A')}")
                    
                    with col2:
                        st.markdown("### 📥 Importador")
                        imp = result.get('partes_involucradas', {}).get('importador', {})
                        st.write(f"**Nombre:** {imp.get('nombre', 'N/A')}")
                        st.write(f"**Tax ID:** {imp.get('tax_id', 'N/A')}")
                    
                    # Mercancías
                    st.markdown("### 📦 Mercancías")
                    mercancias = result.get('mercancias', [])
                    if isinstance(mercancias, list) and mercancias:
                        df = pd.DataFrame(mercancias)
                        st.dataframe(df, use_container_width=True)
                    
                    # Cumplimiento
                    st.markdown("### ⚖️ Análisis de Cumplimiento")
                    cumplimiento = result.get('cumplimiento', {})
                    
                    # Semáforo de cumplimiento
                    issues = cumplimiento.get('campos_faltantes', [])
                    if not issues:
                        st.success("✅ Documento completo - Sin problemas detectados")
                    else:
                        st.warning(f"⚠️ Se encontraron {len(issues)} problemas")
                        for issue in issues:
                            st.write(f"• {issue}")
                    
                    # Botones de acción
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.download_button(
                            "📥 Descargar JSON",
                            data=json.dumps(result, indent=2),
                            file_name=f"analisis_{uploaded_file.name}.json",
                            mime="application/json"
                        )
                    with col2:
                        if st.button("📧 Enviar por Email"):
                            st.info("Función próximamente")
                    with col3:
                        if st.button("🔄 Nuevo Análisis"):
                            st.experimental_rerun()
                    
                except json.JSONDecodeError:
                    # Si no es JSON, mostrar respuesta raw
                    st.markdown("### Análisis Completo")
                    st.write(response.content[0].text)
                
                progress_bar.progress(100)
                status_text.text("✅ Análisis completado!")
                
            except Exception as e:
                st.error(f"❌ Error durante el análisis: {str(e)}")
                st.info("Tip: Verifica que tu API key de Claude esté configurada correctamente")
    
    elif not claude_client:
        st.warning("⚠️ Configura tu API key de Claude para comenzar")
        st.markdown("""
        ### Cómo configurar:
        1. Ve a [console.anthropic.com](https://console.anthropic.com)
        2. Crea una API key
        3. En Streamlit Cloud: Settings → Secrets
        4. Agrega: `ANTHROPIC_API_KEY = "tu-clave-aqui"`
        """)

with tab2:
    st.markdown("### 📊 Dashboard de Análisis")
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Documentos Hoy", "24", "↑ 12%")
    with col2:
        st.metric("Tiempo Promedio", "45s", "↓ 5s")
    with col3:
        st.metric("Precisión", "94.5%", "↑ 1.2%")
    with col4:
        st.metric("Ahorro Mensual", "$4,250", "↑ $350")
    
    # Gráficos (placeholder)
    st.markdown("### Tendencias de Procesamiento")
    chart_data = pd.DataFrame({
        'Fecha': pd.date_range('2024-01-01', periods=30),
        'Documentos': [20 + i + (i % 7) for i in range(30)]
    })
    st.line_chart(chart_data.set_index('Fecha'))

with tab3:
    st.markdown("### 📜 Historial de Documentos")
    st.info("Conecta con Supabase para ver el historial completo")

with tab4:
    st.markdown("### 🔧 Configuración Avanzada")
    
    # Configuración de Claude
    st.markdown("#### Modelo de Claude")
    model = st.selectbox(
        "Selecciona el modelo",
        ["claude-3-sonnet-20240229 (Recomendado)", "claude-3-opus-20240229 (Más potente)", "claude-3-haiku-20240307 (Más rápido)"]
    )
    
    # Plantillas personalizadas
    st.markdown("#### Plantillas de Análisis")
    if st.button("➕ Crear Nueva Plantilla"):
        st.info("Próximamente: Crea plantillas personalizadas para diferentes tipos de documentos")
