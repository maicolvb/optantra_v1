
[![Banner promocional](banner_ia.png)](https://optantra.streamlit.app/)


# 🧠 Optantra IA - Diagnóstico Logístico Inteligente

Una aplicación web inteligente que utiliza IA para diagnosticar y resolver problemas logísticos en tiempo real.

## ✨ Características

- 🤖 **IA Integrada**: Utiliza ChatGPT para análisis inteligente de problemas logísticos
- 📊 **Diagnóstico Detallado**: Análisis completo con soluciones específicas y accionables
- 📈 **Métricas de Impacto**: Estimaciones de tiempo, costo y eficiencia
- ⚡ **Acciones Rápidas**: Recomendaciones inmediatas basadas en el proceso
- 🎨 **Interfaz Moderna**: Diseño responsive y profesional
- 🔒 **Seguro**: Manejo seguro de claves API

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone <tu-repositorio>
cd optantra_v1
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar OpenAI API

#### Opción A: Usando archivo .env (Recomendado)
1. Copia el archivo `env_example.txt` a `.env`
2. Edita `.env` y agrega tu clave de API de OpenAI:
```bash
OPENAI_API_KEY=tu_clave_api_aqui
```

#### Opción B: Configuración manual
- Ejecuta la aplicación y configura tu API key en la barra lateral

### 4. Obtener API Key de OpenAI
1. Ve a [OpenAI Platform](https://platform.openai.com/api-keys)
2. Crea una nueva cuenta o inicia sesión
3. Genera una nueva API key
4. Copia la clave y úsala en la configuración

## 🎯 Uso

### Ejecutar la aplicación
```bash
streamlit run optantra.py
```

### Cómo usar la aplicación

1. **Configurar API Key**: Ingresa tu clave de OpenAI en la barra lateral
2. **Seleccionar Proceso**: Elige el área logística con problemas
3. **Describir Problema**: Proporciona detalles específicos del problema
4. **Configurar Contexto**: Ajusta urgencia, tamaño de empresa, industria, etc.
5. **Generar Diagnóstico**: Haz clic en "Generar Diagnóstico Inteligente"
6. **Revisar Resultados**: Analiza las sugerencias en las pestañas disponibles

## 📋 Procesos Soportados

- 📦 Recibo y entrada de mercancía
- 📊 Control y planeación del inventario
- 🤝 Compras y gestión de proveedores
- 🚚 Alistamiento y despacho de pedidos
- 🏢 Gestión de almacenes
- 🚛 Transporte y distribución
- 🔄 Gestión de devoluciones
- 📈 Análisis de datos y reportes

## 🛠️ Tecnologías Utilizadas

- **Frontend**: Streamlit
- **IA**: OpenAI GPT-3.5-turbo
- **Backend**: Python
- **Estilos**: CSS personalizado
- **Configuración**: python-dotenv

## 🔧 Configuración Avanzada

### Variables de Entorno
```bash
# API Configuration
OPENAI_API_KEY=tu_clave_api
OPENAI_MODEL=gpt-3.5-turbo  # Opcional

# App Configuration
STREAMLIT_SERVER_PORT=8501  # Puerto por defecto
```

### Personalización
- Modifica `optantra.py` para cambiar el prompt de IA
- Ajusta los estilos CSS en la sección de estilos
- Agrega nuevos procesos en la lista `procesos`

## 📊 Estructura del Proyecto

```
optantra_v1/
├── optantra.py          # Aplicación principal
├── requirements.txt     # Dependencias de Python
├── env_example.txt      # Ejemplo de configuración
├── README.md           # Documentación
└── banner_ia.png       # Imagen del banner
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🆘 Soporte

Si encuentras algún problema:

1. Verifica que tu API key de OpenAI sea válida
2. Asegúrate de tener créditos disponibles en tu cuenta de OpenAI
3. Revisa que todas las dependencias estén instaladas correctamente
4. Abre un issue en el repositorio

## 🔮 Próximas Características

- [ ] Integración con bases de datos para historial
- [ ] Análisis de datos en tiempo real
- [ ] Exportación de reportes en PDF
- [ ] Integración con sistemas ERP
- [ ] Chat en tiempo real con IA
- [ ] Análisis predictivo de problemas

---

**Desarrollado con ❤️ usando Streamlit y OpenAI**

