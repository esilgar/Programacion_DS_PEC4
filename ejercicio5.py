"""
Módulo para el Ejercicio 5: Análisis de la UCSC (Unió Ciclista Sant Cugat).
"""

def analizar_ucsc(df):
    """
    Realiza el análisis completo sobre los ciclistas de la UCSC (Unió Ciclista Sant Cugat),
     respondiendo a las preguntas planteadas y muestra los resultados por pantalla:
      - ¿Cuáles son los ciclistas de la UCSC?
      - ¿Qué ciclista de la UCSC ha hecho el mejor tiempo?
      - ¿En qué posición sobre el total ha quedado este ciclista, y qué porcentaje sobre el total representa?

    Args:
        df (pd.DataFrame): DataFrame con los datos de los ciclistas.

    Returns:
        dict: Diccionario con los siguientes elementos:
            - 'ciclistas_ucsc': DataFrame con los ciclistas de la UCSC.
            - 'mejor_ciclista': Series con los datos del mejor ciclista.
            - 'posicion': int, posición del mejor ciclista.
            - 'porcentaje': float, porcentaje sobre el total.
    """
    # Filtrar ciclistas de la UCSC
    df_ucsc = df[df['club_clean'] == 'UCSC'].copy()


    # Verificar si hay ciclistas en la UCSC
    if df_ucsc.empty:
        print("\nNo hay ciclistas en la UCSC.")
        return None

    # Convertir tiempos a segundos para calcular el mejor tiempo
    df_ucsc['time_seconds'] = df_ucsc['time'].apply(
        lambda x: sum(int(unit) * factor for unit, factor in zip(x.split(':'), [3600, 60, 1]))
    )

    # Encontrar el mejor ciclista de la UCSC
    mejor_ciclista = df_ucsc.loc[df_ucsc['time_seconds'].idxmin()]

    # Convertir tiempos a segundos en el DataFrame general
    df['time_seconds'] = df['time'].apply(lambda x: sum(int(unit) * factor for unit, factor in zip(x.split(':'), [3600, 60, 1])))
    df_sorted = df.sort_values(by='time_seconds').reset_index(drop=True)

    # Determinar la posición del mejor ciclista dentro del df ordenado por tiempos de llegada
    posicion = df_sorted[df_sorted['dorsal'] == mejor_ciclista['dorsal']].index[0] + 1

    #total de ciclistas
    print("\ntotal de cilistas:")
    print(len(df))

    # Calcular el porcentaje sobre el total
    porcentaje = (posicion / len(df)) * 100
    # Calcular percentil
    percentil = 100 - porcentaje

    # Mostrar resultados por pantalla
    print("\nCiclistas de la UCSC:")
    print(df_ucsc)

    print("\nMejor ciclista de la UCSC:")
    print(mejor_ciclista)


    print(f"\nEl mejor ciclista de la UCSC quedó en la posición {posicion} sobre el total,\n"
          f" representando el {porcentaje:.2f}% del total.\n"
          f" El corredor se encuentra en el percentil {percentil:.2f}%")

    return {
        'ciclistas_ucsc': df_ucsc,
        'mejor_ciclista': mejor_ciclista,
        'posicion': posicion,
        'porcentaje': porcentaje
    }
