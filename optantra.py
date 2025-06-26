import streamlit as st

procesos = [
    "Recibo y entrada de mercancía",
    "Control y planeación del inventario",
    "Compras y gestión de proveedores",
    "Alistamiento y despacho de pedidos"
]

st.title("🧠 Diagnóstico logístico inteligente")

# Menú desplegable
proceso_elegido = st.selectbox("Selecciona el proceso que presenta problemas:", procesos)

# Entrada de texto
descripcion = st.text_input("Describe el problema")

# Radio buttons
urgencia = st.radio("Nivel de urgencia:", ["Alta", "Media", "Baja"])

# Botón
if st.button("🔍 Generar sugerencia"):
    if proceso_elegido == procesos[1]:
        sugerencia = "⚠️ Implementa una regla mínimo-máximo y una alerta semanal."
    elif proceso_elegido == procesos[2]:
        sugerencia = "💰 Reconsidera los métodos de pago y los tiempos de entrega."
    elif proceso_elegido == procesos[3]:
        sugerencia = "📦 Revise la metodología que está empleando la empresa en el despacho."
    else:
        sugerencia = "🔍 Audita y documenta el flujo para detectar cuellos de botella."

    # Mostrar resultado
    st.markdown(f"""
    ### 🧩 Proceso:  
    {proceso_elegido}

    ### 📝 Problema:  
    {descripcion}

    ### ⚠️ Urgencia:  
    {urgencia}

    ### 💡 Sugerencia automática:  
    {sugerencia}
    """)

