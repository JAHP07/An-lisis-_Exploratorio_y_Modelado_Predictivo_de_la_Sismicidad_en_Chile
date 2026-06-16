"""
Tests para los módulos del proyecto de análisis sísmico.
"""

import pytest
import pandas as pd
import numpy as np
from src.extraccion_datos import limpiar_datos_sismos
from src.analisis import (
    estadistica_descriptiva,
    analizar_relacion_magnitud_profundidad,
    agrupar_sismos,
    analizar_caracteristicas_grupos,
    generar_resumen_kpi
)


@pytest.fixture
def dataframe_ejemplo():
    """Crea un DataFrame de ejemplo para testing."""
    data = {
        'lugar': ['Santiago', 'Valparaíso', 'Concepción', 'La Serena', 'Antofagasta'],
        'magnitud': [4.5, 5.2, 6.1, 4.8, 5.5],
        'fecha': pd.date_range('2025-01-01', periods=5),
        'longitud': [-70.6, -71.6, -73.0, -71.2, -70.4],
        'latitud': [-33.4, -33.0, -36.8, -29.9, -23.6],
        'profundidad': [50.0, 80.0, 120.0, 45.0, 200.0]
    }
    return pd.DataFrame(data)


class TestExtraccionDatos:
    """Tests para el módulo de extracción de datos."""
    
    def test_limpiar_datos_no_elimina_completos(self, dataframe_ejemplo):
        """Verifica que no se eliminen datos cuando están completos."""
        limpio = limpiar_datos_sismos(dataframe_ejemplo)
        assert len(limpio) == len(dataframe_ejemplo)
    
    def test_limpiar_datos_manaja_valores_faltantes(self):
        """Verifica que se manejen valores faltantes correctamente."""
        data = {
            'lugar': ['A', 'B', 'C'],
            'magnitud': [4.5, None, 5.0],
            'fecha': pd.date_range('2025-01-01', periods=3),
            'longitud': [-70.0, -71.0, -72.0],
            'latitud': [-33.0, -34.0, -35.0],
            'profundidad': [50.0, 60.0, 70.0]
        }
        df = pd.DataFrame(data)
        limpio = limpiar_datos_sismos(df)
        assert len(limpio) == 2
    
    def test_limpiar_datos_filtra_magnitud_negativa(self):
        """Verifica que se filtren magnitudes negativas."""
        data = {
            'lugar': ['A', 'B', 'C'],
            'magnitud': [4.5, -1.0, 5.0],
            'fecha': pd.date_range('2025-01-01', periods=3),
            'longitud': [-70.0, -71.0, -72.0],
            'latitud': [-33.0, -34.0, -35.0],
            'profundidad': [50.0, 60.0, 70.0]
        }
        df = pd.DataFrame(data)
        limpio = limpiar_datos_sismos(df)
        assert len(limpio) == 2


class TestAnalisis:
    """Tests para el módulo de análisis."""
    
    def test_estadistica_descriptiva_retorna_dataframe(self, dataframe_ejemplo):
        """Verifica que las estadísticas descriptivas retornen un DataFrame."""
        stats = estadistica_descriptiva(dataframe_ejemplo)
        assert isinstance(stats, pd.DataFrame)
        assert 'magnitud' in stats.columns or 'magnitud' in stats.index
    
    def test_relacion_magnitud_profundidad_retorna_dict(self, dataframe_ejemplo):
        """Verifica que el análisis de relación retorne un diccionario."""
        resultado = analizar_relacion_magnitud_profundidad(dataframe_ejemplo)
        assert isinstance(resultado, dict)
        assert 'correlacion' in resultado
        assert 'r2' in resultado
    
    def test_agrupar_sismos_retorna_forma_correcta(self, dataframe_ejemplo):
        """Verifica que el clustering retorne la forma correcta."""
        etiquetas, modelo = agrupar_sismos(dataframe_ejemplo, n_grupos=2)
        assert len(etiquetas) == len(dataframe_ejemplo)
        assert len(np.unique(etiquetas)) == 2
    
    def test_analizar_caracteristicas_grupos_retorna_dataframe(self, dataframe_ejemplo):
        """Verifica que el análisis de grupos retorne un DataFrame."""
        etiquetas, _ = agrupar_sismos(dataframe_ejemplo, n_grupos=2)
        cluster_stats = analizar_caracteristicas_grupos(dataframe_ejemplo, etiquetas)
        assert isinstance(cluster_stats, pd.DataFrame)
        assert len(cluster_stats) == 2
    
    def test_generar_resumen_kpi_retorna_dict_con_claves(self, dataframe_ejemplo):
        """Verifica que los KPIs tengan las llaves esperadas."""
        kpis = generar_resumen_kpi(dataframe_ejemplo)
        assert isinstance(kpis, dict)
        assert 'total_sismos' in kpis
        assert 'magnitud_promedio' in kpis
        assert 'magnitud_maxima' in kpis
        assert kpis['total_sismos'] == 5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
