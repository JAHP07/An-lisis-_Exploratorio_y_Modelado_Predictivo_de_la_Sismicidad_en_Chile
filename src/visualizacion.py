"""
Módulo de visualización de datos sísmicos.

Este módulo proporciona funciones para generar visualizaciones profesionales
de datos sísmicos, incluyendo distribuciones, relaciones y mapas geográficos.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Optional, Tuple
import os


def graficar_distribucion_magnitud(
    df: pd.DataFrame,
    figsize: Tuple[int, int] = (10, 5),
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Genera un histograma de la distribución de magnitudes.
    
    Args:
        df: DataFrame con los datos sísmicos.
        figsize: Tamaño de la figura (ancho, alto).
        save_path: Ruta opcional para guardar la imagen.
    
    Returns:
        Figura de matplotlib con el gráfico.
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.histplot(data=df, x='magnitud', bins=10, kde=True, color="crimson", ax=ax)
    ax.set_title('Distribución de Magnitudes de Sismos Recientes en Chile', fontsize=14)
    ax.set_xlabel('Magnitud')
    ax.set_ylabel('Frecuencia')
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def graficar_profundidad_vs_magnitud(
    df: pd.DataFrame,
    figsize: Tuple[int, int] = (10, 5),
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Genera un scatter plot de profundidad vs magnitud.
    
    Args:
        df: DataFrame con los datos sísmicos.
        figsize: Tamaño de la figura (ancho, alto).
        save_path: Ruta opcional para guardar la imagen.
    
    Returns:
        Figura de matplotlib con el gráfico.
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.scatterplot(
        data=df, x='magnitud', y='profundidad',
        size='magnitud', sizes=(50, 200), alpha=0.7, ax=ax
    )
    ax.invert_yaxis()
    ax.set_title('Profundidad vs Magnitud del Sismo', fontsize=14)
    ax.set_xlabel('Magnitud')
    ax.set_ylabel('Profundidad (km)')
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def graficar_distribucion_geografica(
    df: pd.DataFrame,
    figsize: Tuple[int, int] = (6, 8),
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Genera un mapa de dispersión geográfica de los epicentros.
    
    Args:
        df: DataFrame con los datos sísmicos.
        figsize: Tamaño de la figura (ancho, alto).
        save_path: Ruta opcional para guardar la imagen.
    
    Returns:
        Figura de matplotlib con el gráfico.
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.scatterplot(
        data=df, x='longitud', y='latitud',
        hue='magnitud', size='magnitud',
        sizes=(40, 250), palette='flare', alpha=0.8, ax=ax
    )
    ax.set_title('Distribución Geográfica de Sismos', fontsize=14)
    ax.set_xlabel('Longitud')
    ax.set_ylabel('Latitud')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def generar_todas_visualizaciones(
    df: pd.DataFrame,
    output_dir: str = "output"
) -> dict:
    """
    Genera todas las visualizaciones y las guarda en el directorio especificado.
    
    Args:
        df: DataFrame con los datos sísmicos.
        output_dir: Directorio donde se guardarán las imágenes.
    
    Returns:
        Diccionario con las rutas de las imágenes generadas.
    """
    paths = {
        'distribucion_magnitud': os.path.join(output_dir, 'distribucion_magnitud.png'),
        'profundidad_vs_magnitud': os.path.join(output_dir, 'profundidad_vs_magnitud.png'),
        'distribucion_geografica': os.path.join(output_dir, 'distribucion_geografica.png')
    }
    
    graficar_distribucion_magnitud(df, save_path=paths['distribucion_magnitud'])
    graficar_profundidad_vs_magnitud(df, save_path=paths['profundidad_vs_magnitud'])
    graficar_distribucion_geografica(df, save_path=paths['distribucion_geografica'])
    
    return paths


if __name__ == "__main__":
    from src.extraccion_datos import obtener_datos_sismos, limpiar_datos_sismos
    
    df = obtener_datos_sismos()
    df = limpiar_datos_sismos(df)
    
    paths = generar_todas_visualizaciones(df)
    print("Visualizaciones generadas:")
    for name, path in paths.items():
        print(f"  - {name}: {path}")
