import os
import json

def crear_estructura():
    print("🚀 Iniciando la creación automática del repositorio...")
    
    # 1. Crear carpetas si no existen
    os.makedirs('.devcontainer', exist_ok=True)
    os.makedirs('notebooks', exist_ok=True)
    print("📁 Carpetas creadas: .devcontainer, notebooks")

    # 2. Crear archivo .devcontainer/devcontainer.json
    devcontainer_data = {
        "name": "Analisis Sismico Chile - Codespace",
        "image": "mcr.microsoft.com/devcontainers/python:3.11",
        "customizations": {
            "vscode": {
                "extensions": [
                    "ms-toolsai.jupyter",
                    "ms-python.python",
                    "ms-python.vscode-pylance"
                ]
            }
        },
        "postCreateCommand": "pip install -r requirements.txt"
    }
    with open('.devcontainer/devcontainer.json', 'w', encoding='utf-8') as f:
        json.dump(devcontainer_data, f, indent=4, ensure_ascii=False)
    print("📄 Archivo creado: .devcontainer/devcontainer.json")

    # 3. Crear archivo requirements.txt
    requirements_data = "requests>=2.31.0\npandas>=2.2.0\nmatplotlib>=3.8.0\nseaborn>=0.13.0\nnotebook>=7.1.0\n"
    with open('requirements.txt', 'w', encoding='utf-8') as f:
        f.write(requirements_data)
    print("📄 Archivo creado: requirements.txt")

    # 4. Crear archivo README.md
    readme_data = """# 🌋 Análisis Sísmico de Chile

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
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_data)
    print("📄 Archivo creado: README.md")

    # 5. Crear archivo notebooks/analisis_sismico.ipynb
    notebook_data = {
     "cells": [
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
        "# 🌋 Análisis Sísmico de Chile\n",
        "**Proyecto de Portafolio**\n",
        "\n",
        "Este notebook se conecta a la API de Boostr para descargar, limpiar y analizar visualmente los sismos más recientes del país."
       ]
      },
      {
       "cell_type": "code",
       "execution_count": None,
       "metadata": {},
       "outputs": [],
       "source": [
        "import requests\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "# Configuración de estilo\n",
        "sns.set_theme(style=\"darkgrid\", palette=\"mako\")\n",
        "print(\"Librerías importadas correctamente.\")"
       ]
      },
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
        "### 1. Extracción de Datos vía API"
       ]
      },
      {
       "cell_type": "code",
       "execution_count": None,
       "metadata": {},
       "outputs": [],
       "source": [
        "url = \"https://api.boostr.cl/earthquakes.json\"\n",
        "headers = {\"accept\": \"application/json\"}\n",
        "\n",
        "print(\"Conectando con la API...\")\n",
        "response = requests.get(url, headers=headers)\n",
        "\n",
        "if response.status_code == 200:\n",
        "    sismos_data = response.json().get('data', [])\n",
        "    print(f\"¡Éxito! Se obtuvieron {len(sismos_data)} registros sísmicos.\")\n",
        "else:\n",
        "    print(f\"Error en la petición. Código de estado: {response.status_code}\")"
       ]
      },
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
        "### 2. Transformación y Limpieza con Pandas"
       ]
      },
      {
       "cell_type": "code",
       "execution_count": None,
       "metadata": {},
       "outputs": [],
       "source": [
        "df = pd.DataFrame(sismos_data)\n",
        "\n",
        "# Limpieza de tipos de datos\n",
        "df['magnitude'] = pd.to_numeric(df['magnitude'], errors='coerce')\n",
        "df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')\n",
        "df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')\n",
        "\n",
        "if df['depth'].dtype == object:\n",
        "    df['depth'] = df['depth'].str.replace(' km', '', regex=False)\n",
        "df['depth'] = pd.to_numeric(df['depth'], errors='coerce')\n",
        "df['date'] = pd.to_datetime(df['date'])\n",
        "\n",
        "print(\"Estructura del DataFrame procesado:\")\n",
        "df.info()\n",
        "display(df.head())"
       ]
      },
      {
       "cell_type": "markdown",
       "metadata": {},
       "source": [
        "### 3. Visualización de Datos (EDA)"
       ]
      },
      {
       "cell_type": "code",
       "execution_count": None,
       "metadata": {},
       "outputs": [],
       "source": [
        "# Gráfico 1: Distribución de Magnitudes\n",
        "plt.figure(figsize=(10, 5))\n",
        "sns.histplot(data=df, x='magnitude', bins=10, kde=True, color=\"crimson\")\n",
        "plt.title('Distribución de Magnitudes de Sismos Recientes en Chile', fontsize=14)\n",
        "plt.xlabel('Magnitud')\n",
        "plt.ylabel('Frecuencia')\n",
        "plt.show()"
       ]
      },
      {
       "cell_type": "code",
       "execution_count": None,
       "metadata": {},
       "outputs": [],
       "source": [
        "# Gráfico 2: Profundidad vs Magnitud\n",
        "plt.figure(figsize=(10, 5))\n",
        "sns.scatterplot(data=df, x='magnitude', y='depth', size='magnitude', sizes=(50, 200), alpha=0.7)\n",
        "plt.gca().invert_yaxis()  # Invertir eje Y para simular profundidad subterránea\n",
        "plt.title('Profundidad vs Magnitud del Sismo', fontsize=14)\n",
        "plt.xlabel('Magnitud')\n",
        "plt.ylabel('Profundidad (km)')\n",
        "plt.show()"
       ]
      },
      {
       "cell_type": "code",
       "execution_count": None,
       "metadata": {},
       "outputs": [],
       "source": [
        "# Gráfico 3: Dispersión Geográfica de los Epicentros\n",
        "plt.figure(figsize=(6, 8))\n",
        "sns.scatterplot(data=df, x='longitude', y='latitude', hue='magnitude', size='magnitude', sizes=(40, 250), palette='flare', alpha=0.8)\n",
        "plt.title('Distribución Geográfica de Sismos', fontsize=14)\n",
        "plt.xlabel('Longitud')\n",
        "plt.ylabel('Latitud')\n",
        "plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')\n",
        "plt.tight_layout()\n",
        "plt.show()"
       ]
      }
     ],
     "metadata": {
      "language_info": {
       "name": "python"
      }
     },
     "nbformat": 4,
     "nbformat_minor": 2
    }
    with open('notebooks/analisis_sismico.ipynb', 'w', encoding='utf-8') as f:
        json.dump(notebook_data, f, indent=4, ensure_ascii=False)
    print("📄 Archivo creado: notebooks/analisis_sismico.ipynb")

    print("\n✨ ¡Todo listo! Tu entorno y el perfil del proyecto han sido generados exitosamente.")

if __name__ == '__main__':
    crear_estructura()