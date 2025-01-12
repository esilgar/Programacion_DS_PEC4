"""
Módulo para el Ejercicio 3: Agrupamiento de minutos y generación de histograma.
"""
import os
import matplotlib.pyplot as plt

def minutes_002040(time_str):
    """
    Agrupa un tiempo en formato hh:mm:ss a franjas de 20 minutos.

    Args:
        time_str (str): Tiempo en formato hh:mm:ss.

    Returns:
        str: Tiempo en formato hh:mm, donde los minutos son 00, 20 o 40.
    """
    try:
        # Separar horas, minutos y segundos
        h, m, _ = map(int, time_str.split(":"))

        # Agrupar minutos
        if m < 20:
            grouped_minutes = "00"
        elif m < 40:
            grouped_minutes = "20"
        else:
            grouped_minutes = "40"

        return f"{h:02}:{grouped_minutes}"
    except Exception as e:
        raise ValueError(f"Error procesando el tiempo '{time_str}': {e}") from e

def procesar_tiempos(df):
    """
    Procesa los tiempos de un DataFrame para crear una columna agrupada y genera un histograma.

    Args:
        df (pd.DataFrame): DataFrame original con la columna 'time'.

    Returns:
        pd.DataFrame: DataFrame con agrupamiento por franjas de 20 minutos.
    """
    # Crear nueva columna agrupada
    df = df.copy()
    df['time_grouped'] = df['time'].apply(minutes_002040)

    # Mostrar los 15 primeros valores
    print("Primeros 15 valores del DataFrame con la columna agrupada:")
    print(df.head(15))

    # Agrupamiento por columna 'time_grouped'
    grouped_df = df.groupby('time_grouped').size().reset_index(name='count')

    # Mostrar agrupamiento
    print("\nAgrupamiento por time_grouped:")
    print(grouped_df)

    # Generar histograma
    os.makedirs("img", exist_ok=True)  # Crear carpeta si no existe
    plt.figure(figsize=(10, 6))
    plt.bar(grouped_df['time_grouped'], grouped_df['count'], width=0.5)
    plt.title("Histograma de tiempos agrupados")
    plt.xlabel("Franja de tiempo (hh:mm)")
    plt.ylabel("Número de ciclistas")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig("img/histograma.png")
    print("\nHistograma guardado en 'img/histograma.png'.")

    return grouped_df
