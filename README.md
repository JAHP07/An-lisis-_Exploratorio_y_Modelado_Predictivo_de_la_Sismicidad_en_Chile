# 🌋 Análisis Sísmico de Chile

**Proyecto de Portafolio: EDA + Visualización de Datos en Tiempo Real**

Este proyecto realiza un Análisis Exploratorio de Datos (EDA) sobre la actividad sísmica reciente en Chile. Automatiza la extracción de datos desde una API REST pública, realiza transformaciones y limpieza con Pandas, y genera visualizaciones avanzadas sobre la frecuencia, magnitud y distribución geográfica de los sismos utilizando Seaborn y Matplotlib.

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.11
- **Entorno:** GitHub Codespaces / Jupyter Notebooks
- **Librerías Principales:** Pandas, NumPy, Requests, Matplotlib, Seaborn
- **Fuente de Datos:** API de Boostr (`https://api.boostr.cl/earthquakes.json`)

## 📁 Estructura del Repositorio
- `.devcontainer/`: Configuración automatizada para levantar el entorno listo en GitHub Codespaces.
- `notebooks/`: Contiene el Jupyter Notebook principal con el paso a paso del análisis.
- `requirements.txt`: Lista de dependencias del proyecto.

## 🚀 Configuración del Entorno en GitHub Codespaces
Este repositorio está completamente configurado para usarse con un solo clic:
1. Haz clic en el botón **Code** en GitHub.
2. Ve a la pestaña **Codespaces** y selecciona **Create codespace on main**.
3. El entorno instalará automáticamente Python, las extensiones de Jupyter y todas las librerías necesarias (`pandas`, `seaborn`, etc.).
4. Abre el archivo `notebooks/analisis_sismico.ipynb` y presiona **Run All**.

## 📊 Objetivos del Análisis
1. **Distribución de Magnitudes:** Evaluar el comportamiento de las magnitudes registradas.
2. **Relación Magnitud-Profundidad:** Analizar si los sismos más profundos tienden a liberar mayor o menor energía.
3. **Distribución Geográfica:** Mapear los epicentros utilizando coordenadas de latitud y longitud.
