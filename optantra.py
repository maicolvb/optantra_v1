# -*- coding: utf-8 -*-
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Optantra", layout="wide")

st.title("📦 Optantra - Diagnóstico de Procesos Logísticos")
st.subheader("Selecciona el proceso que deseas analizar y recibe una recomendación")

# Lista de procesos
procesos = [
    "Recibo y entrada de mercancía",
    "Control y planeación del inventario",
    "Compras y gestión de proveedores",
    "Alistamiento y despacho de pedidos",
    "Atención al cliente / PQRS",
    "Tareas administrativas internas",
    "Reportes, indicadores y análisis",
    "Otro"
]

# Interfaz de selección
proceso_elegido = st.selectbox("🛠️ Selecciona un proceso logístico", procesos)

descripcion = st.text_input("✏️ Describe brevemente el problema")
urgencia = st.radio("⚠️ Nivel de urgencia", ["Alta", "Media", "Baja"])

# Generar recomendación
if proceso_elegido == procesos[1]:
    sugerencia = "📌 Implementa una regla mínimo-máximo y una alerta semanal."
elif proceso_elegido == procesos[2]:
    sugerencia = "🔄 Reconsidera los métodos de pago y los tiempos de entrega."
else:
    sugerencia = "🔍 Audita y documenta el flujo para detectar cuellos de botella."

# Mostrar resultado
if descripcion:
    st.markdown("---")
    st.success(f"🔧 Recomendación para **{proceso_elegido}**:\n\n{sugerencia}")
    st.info(f"📝 Descripción: {descripcion} \n\n🚨 Urgencia: {urgencia}")

