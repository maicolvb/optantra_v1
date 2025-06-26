import streamlit as st

# Lista de procesos
procesos = [
    "Recibo y entrada de mercancía",
    "Control y planeación del inventario",
    "Compras y gestión de proveedores",
    "Alistamiento y despacho de pedidos"
]

# Interfaz
st.title("💼 Optantra - Sugerencias logísticas")
proceso_elegido = st.selectbox("Selecciona un proceso logístico:", procesos)
descripcion = st.text_input("Describe el problema:")
urgencia = st.selectbox("Nivel de urgencia:", ["Alta", "Media", "Baja"])

# Lógica de sugerencias
if proceso_elegido == procesos[0]:
    sugerencia = "✅ Asegura un buen registro y verificación de mercancía entrante."
elif proceso_elegido == procesos[1]:
    sugerencia = "📊 Implementa una regla mínimo-máximo y una alerta semanal."
elif proceso_elegido == procesos[2]:
    sugerencia = "💰 Reconsidera los métodos de pago y tiempos de entrega."
elif proceso_elegido == procesos[3]:
    sugerencia = "🚚 Revisa la metodología de alistamiento y tiempos de despacho."
else:
    sugerencia = "🛠️ Audita y documenta el flujo para detectar cuellos de botella."

# Resultado
st.markdown("---")
st.subheader("🔍 Diagnóstico generado:")
st.write(f"**Proceso:** {proceso_elegido}")
st.write(f"**Problema:** {descripcion}")
st.write(f"**Urgencia:** {urgencia}")
st.success(f"**Sugerencia automática:** {sugerencia}")
