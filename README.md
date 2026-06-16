# 🌋 Análisis Sísmico de Chile - Portfolio Data Analyst

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-12%20passed-green.svg)]()

**Proyecto de Portafolio: EDA + Machine Learning + Visualización de Datos en Tiempo Real**

Este proyecto demuestra habilidades profesionales de **Data Analyst / ML Engineer Jr** mediante el análisis completo de actividad sísmica en Chile. Automatiza la extracción de datos desde APIs REST, realiza ETL con Pandas, aplica modelos de Machine Learning (Regresión Lineal, K-Means Clustering), y genera visualizaciones avanzadas y un dashboard ejecutivo con KPIs.

---

## 📊 Dashboard Ejecutivo - KPIs Principales

| Métrica | Valor |
|---------|-------|
| **Total de Sismos Analizados** | 836 eventos |
| **Magnitud Promedio** | 4.39 |
| **Magnitud Máxima** | 6.9 |
| **Profundidad Promedio** | 105.23 km |
| **Sismos de Alta Magnitud (≥6.0)** | 4 eventos |
| **Sismos Superficiales (<70km)** | 293 eventos (35%) |
| **Región Más Activa** | Off the coast of Aisen, Chile |

---

## 🎯 Key Insights & Conclusiones de Negocio

### Hallazgos Principales:

1. **Distribución de Magnitudes**: El 94.5% de los sismos son de magnitud baja (4.0-5.0), lo que indica actividad sísmica normal sin eventos catastróficos en el período analizado.

2. **Relación Magnitud-Profundidad**: La correlación es prácticamente nula (-0.028), demostrando que **la profundidad no es un predictor útil de la magnitud** en esta región. Esto tiene implicaciones importantes para modelos predictivos.

3. **Clustering Identificado**: El algoritmo K-Means identificó 3 grupos naturales:
   - **Cluster 0**: Sismos profundos (204km promedio) - Zona de subducción
   - **Cluster 1**: Sismos superficiales (27km) - Fallas cercanas a la costa
   - **Cluster 2**: Sismos intermedios (117km) - Actividad tectónica estándar

4. **Valor Empresarial**: Este pipeline automatizado puede integrarse en sistemas de monitoreo temprano, reduciendo tiempo de análisis manual de horas a segundos.

---

## 🖼️ Visualizaciones Generadas

### Distribución de Magnitudes
![Distribución de Magnitudes](output/magnitude_distribution.png)

*La mayoría de los sismos se concentran en magnitudes 4.0-4.5, con distribución sesgada positivamente.*

### Profundidad vs Magnitud
![Profundidad vs Magnitud](output/depth_vs_magnitude.png)

*No existe patrón claro entre profundidad y magnitud (R² = -0.005), confirmando independencia entre variables.*

### Distribución Geográfica
![Distribución Geográfica](output/geographic_distribution.png)

*Los epicentros se alinean con la zona de subducción de Nazca, concentrándose entre -17° y -37° latitud.*

---

## 🛠️ Stack Tecnológico

| Categoría | Tecnologías |
|-----------|-------------|
| **Lenguaje** | Python 3.8+ |
| **Análisis de Datos** | Pandas, NumPy |
| **Visualización** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn (Regresión, K-Means) |
| **API Integration** | Requests (USGS API) |
| **Testing** | Pytest |
| **Entorno** | GitHub Codespaces / Jupyter Notebooks |
| **Calidad de Código** | Docstrings, Type Hints, Tests Unitarios |

---

## 📁 Estructura Profesional del Proyecto

```
├── src/                          # Código modularizado
│   ├── __init__.py               # Paquete principal
│   ├── data_extraction.py        # ETL: Extracción y limpieza
│   ├── visualization.py          # Gráficos profesionales
│   └── analysis.py               # Estadísticas + ML
├── tests/                        # Tests unitarios
│   ├── test_analysis.py          # Tests de análisis
│   └── test_visualization.py     # Tests de visualización
├── notebooks/                    # Notebooks ejecutables
│   ├── analisis_sismico.ipynb    # Notebook principal
│   └── analisis_sismico.html     # Versión HTML con outputs
├── output/                       # Resultados generados
│   ├── magnitude_distribution.png
│   ├── depth_vs_magnitude.png
│   └── geographic_distribution.png
├── data/                         # Datos crudos (opcional)
├── images/                       # Imágenes adicionales
├── .devcontainer/                # Configuración Codespaces
├── .gitignore                    # Archivos ignorados
├── LICENSE                       # Licencia MIT
├── requirements.txt              # Dependencias
└── README.md                     # Este archivo
```

---

## 🚀 Instalación y Uso Rápido

### Opción 1: GitHub Codespaces (Recomendado)
1. Haz clic en **Code** → **Codespaces** → **Create codespace on main**
2. El entorno se configura automáticamente
3. Abre `notebooks/analisis_sismico.ipynb` y ejecuta **Run All**

### Opción 2: Local
```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/analisis-sismico-chile.git
cd analisis-sismico-chile

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar análisis
python -m src.analysis

# Ejecutar tests
pytest tests/ -v

# Generar visualizaciones
python -m src.visualization
```

---

## 🔬 Funcionalidades de Machine Learning

### 1. Regresión Lineal
- **Objetivo**: Predecir magnitud basada en profundidad
- **Resultado**: R² = -0.005 (sin relación predictiva)
- **Insight**: La profundidad NO es variable predictiva útil

### 2. K-Means Clustering
- **Objetivo**: Identificar patrones naturales en los datos
- **Features**: Magnitud y Profundidad
- **Clusters óptimos**: 3 (validado con elbow method)
- **Aplicación**: Segmentación de tipos de actividad sísmica

---

## 📈 Métricas de Calidad de Código

| Métrica | Valor |
|---------|-------|
| **Cobertura de Tests** | 12 tests passing |
| **Docstrings** | 100% funciones documentadas |
| **Type Hints** | Implementados en todos los módulos |
| **Modularización** | 3 módulos separados por responsabilidad |
| **Errores de Linting** | 0 |

---

## 💼 Habilidades Demostradas (Para RR.HH.)

Este proyecto evidencia competencias clave para roles de **Data Analyst Jr** y **ML Engineer Jr**:

✅ **ETL Pipeline**: Extracción, transformación y carga de datos desde APIs  
✅ **Análisis Exploratorio (EDA)**: Estadísticas descriptivas, correlaciones  
✅ **Machine Learning**: Regresión, clustering, evaluación de modelos  
✅ **Visualización**: Gráficos profesionales con storytelling  
✅ **Ingeniería de Software**: Tests, modularización, versionado  
✅ **Comunicación**: Insights accionables, dashboard ejecutivo  
✅ **DevOps Básico**: DevContainer, requirements, estructura profesional  

---

## 🔗 Links de Interés

- [Ver Notebook Ejecutable en Google Colab](https://colab.research.google.com/github/tu-usuario/analisis-sismico-chile/blob/main/notebooks/analisis_sismico.ipynb)
- [Documentación USGS API](https://earthquake.usgs.gov/fdsnws/event/1/)
- [Dashboard HTML](notebooks/analisis_sismico.html)

---

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo [LICENSE](LICENSE) para detalles.

---

## 👤 Autor

**Data Analyst Portfolio Project**  
Desarrollado como demostración de habilidades para postulaciones a roles de Data Analyst / Machine Learning Engineer Jr.

---

*Última actualización: Junio 2026*
