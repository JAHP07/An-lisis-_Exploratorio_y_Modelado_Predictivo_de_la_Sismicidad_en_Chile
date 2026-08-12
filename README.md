# 🌋 Análisis Sísmico de Chile - Portfolio Data Analyst

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/JAHP07/An-lisis-Exploratorio-y-Modelado-Predictivo-de-Datos-S-smicos-en-Chile/actions/workflows/ci.yml/badge.svg)](https://github.com/JAHP07/An-lisis-Exploratorio-y-Modelado-Predictivo-de-Datos-S-smicos-en-Chile/actions/workflows/ci.yml)

**Proyecto de Portafolio: EDA + Machine Learning + Visualización de Datos en Tiempo Real**

Este proyecto demuestra habilidades profesionales de **Data Analyst / ML Engineer Jr** mediante el análisis completo de actividad sísmica en Chile. Automatiza la extracción de datos desde APIs REST, realiza ETL con Pandas, aplica modelos de Machine Learning (Regresión Lineal, K-Means Clustering), y genera visualizaciones avanzadas y un dashboard ejecutivo con KPIs.

---

## 📊 Dashboard Ejecutivo - KPIs Principales

| Métrica | Valor |
|---------|-------|
| **Total de Sismos Analizados** | 820 eventos |
| **Magnitud Promedio** | 4.39 |
| **Magnitud Máxima** | 6.9 |
| **Profundidad Promedio** | 102.09 km |
| **Sismos de Alta Magnitud (≥6.0)** | 4 eventos |
| **Sismos Superficiales (<70km)** | 299 eventos (36%) |
| **Región Más Activa** | Off the coast of Aisen, Chile |

---

## 🎯 Key Insights & Conclusiones de Negocio

### Hallazgos Principales:

1. **Distribución de Magnitudes**: El 94.4% de los sismos son de magnitud baja (4.0-5.0), lo que indica actividad sísmica normal sin eventos catastróficos en el período analizado.

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
│   ├── extraccion_datos.py       # ETL: Extracción y limpieza
│   ├── visualizacion.py          # Gráficos profesionales
│   └── analisis.py               # Estadísticas + ML
├── tests/                        # Tests unitarios
│   ├── test_analisis.py          # Tests de extracción y análisis
│   └── test_visualizacion.py     # Tests de visualización
├── notebooks/
│   └── analisis_sismico.ipynb    # Notebook principal ejecutable
├── output/                       # Resultados generados
│   ├── magnitude_distribution.png
│   ├── depth_vs_magnitude.png
│   └── geographic_distribution.png
├── .github/workflows/ci.yml      # CI: pytest automático
├── .devcontainer/                # Configuración Codespaces
├── .gitignore                    # Archivos ignorados
├── LICENSE                       # Licencia MIT
├── requirements.txt              # Dependencias
└── README.md                     # Este archivo
```



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

- [Ver Notebook Ejecutable en Google Colab](https://colab.research.google.com/github/JAHP07/An-lisis-Exploratorio-y-Modelado-Predictivo-de-Datos-S-smicos-en-Chile/blob/main/notebooks/analisis_sismico.ipynb)
- [Documentación USGS API](https://earthquake.usgs.gov/fdsnws/event/1/)

---

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo [LICENSE](LICENSE) para detalles.

---

## 👤 Autor

**Jonathan Huenuanca** — Ingeniero en Informática  
Proyecto de portafolio desarrollado como demostración de habilidades en análisis de datos y machine learning.

- [GitHub](https://github.com/JAHP07)
- [LinkedIn](https://www.linkedin.com/in/jonathanhuenuanca)

---

*Última actualización: Junio 2026*
