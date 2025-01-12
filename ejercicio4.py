"""
Módulo para el Ejercicio 4: Club Ciclistas.
"""
import re



def clean_club(club):
    """
    Limpia el nombre del club ciclista según las reglas especificadas.

    Args:
        club (str): Nombre del club original.

    Returns:
        str: Nombre del club limpio.
    """
    if not isinstance(club, str):
        return "INDEPENDIENTE"

    # Convertir a mayúsculas
    club = club.upper()

    # Reemplazar frases completas
    club = re.sub(r'(PEÑA CICLISTA |PENYA CICLISTA |AGRUPACIÓN CICLISTA |AGRUPACION CICLISTA |'
                   r'AGRUPACIÓ CICLISTA |AGRUPACIO CICLISTA |CLUB CICLISTA |CLUB )', '', club)

    # Reemplazar prefijos específicos
    club = re.sub(r'^(C\.C\. |C\.C |CC |C\.D\. |C\.D |CD |A\.C\. |A\.C |AC |'
                   r'A\.D\. |A\.D |AD |A\.E\. |A\.E |AE |E\.C\. |E\.C |EC |'
                   r'S\.C\. |S\.C |SC |S\.D\. |S\.D |SD )', '', club)

    # Reemplazar sufijos específicos
    club = re.sub(r'( T\.T\.| T\.T| TT| T\.E\.| T\.E| TE| C\.C\.| C\.C| CC|'
                   r' C\.D\.| C\.D| CD| A\.D\.| A\.D| AD| A\.C\.| A\.C| AC)$', '', club)

    # Eliminar espacios al inicio y al final
    club = club.strip()

    return club or "INDEPENDIENTE"

def procesar_clubs(df):
    """
    Limpia los nombres de los clubs en el DataFrame, agrupa los datos y los ordena.

    Args:
        df (pd.DataFrame): DataFrame original con la columna 'club'.

    Returns:
        pd.DataFrame: DataFrame agrupado y ordenado por número de participantes por club.
    """
    # Crear una nueva columna con los nombres limpios
    df = df.copy()
    df['club_clean'] = df['club'].apply(clean_club)

    # Mostrar los 15 primeros valores
    print("Primeros 15 valores del DataFrame con los clubs limpios:")
    print(df.head(15))

    # Agrupar por club_clean
    grouped_df = df.groupby('club_clean').size().reset_index(name='participants')

    # Ordenar por número de participantes en orden descendente
    grouped_df = grouped_df.sort_values(by='participants', ascending=False)

    # Mostrar los resultados
    print("\nClubs con más participantes:")
    print(grouped_df.head(15))

    return df
