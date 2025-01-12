"""
Módulo con las funciones del ejercicio 1: Importación del dataset y EDA.
"""
import pandas as pd


def importar_dataset(ruta_csv):
    """
    Importa un archivo CSV a un DataFrame.

    Args:
        ruta_csv (str): Ruta al archivo CSV.
        pandas_module (module): Módulo pandas para la lectura.

    Returns:
        pd.DataFrame: DataFrame con los datos del CSV.
    """
    return pd.read_csv(ruta_csv, delimiter=';')


def analizar_dataset(data):
    """
    Realiza el análisis exploratorio de datos (EDA) del dataset.

    Args:
        data (pd.DataFrame): DataFrame con los datos del dataset.

    Returns:
        None
    """
    # Mostrar los 5 primeros registros
    print("\nPrimeros 5 registros del dataset:")
    print(data.head())

    # ¿Cuántos ciclistas participaron?
    total_ciclistas = len(data)
    print(f"\nNúmero total de ciclistas que participaron: {total_ciclistas}")

    # ¿Qué columnas tiene el dataset?
    columnas = list(data.columns)
    print(f"\nColumnas disponibles en el dataset: {columnas}")


def ejecutar_ejercicio1(ruta_csv):
    """
    Ejecuta las operaciones del Ejercicio 1: Importación y Análisis Exploratorio de Datos (EDA).

    Args:
        ruta_csv (str): Ruta al archivo CSV.

    Returns:
        pd.DataFrame: DataFrame con los datos importados.
    """
    print("EJERCICIO 1: Importación del dataset y EDA")
    data = importar_dataset(ruta_csv)

    if data is not None:
        analizar_dataset(data)

    return data
