"""
Módulo con las funciones del ejercicio 2: Anonimizar los ciclistas y limpieza del dataset.
"""
from faker import Faker

faker = Faker()

def name_surname(df):
    """
    Anonimiza los nombres de los ciclistas en la columna 'biker'.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos originales.
    
    Returns:
        pd.DataFrame: DataFrame con los nombres anonimizados.
    """
    # Reemplazar directamente los valores de la columna 'biker'

    df = df.copy()
    df['biker'] = df['biker'].apply(lambda _: f"{faker.first_name()} {faker.last_name()}")
    return df

def eliminar_no_participantes(df):
    """
    Elimina a los ciclistas que tienen tiempo '00:00:00'.
    
    Args:
        df (pd.DataFrame): DataFrame original.
    
    Returns:
        pd.DataFrame: DataFrame sin los ciclistas que no participaron.
    """
    df = df.copy()
    return df[df['time'] != '00:00:00']

def filtrar_por_dorsal(df, dorsal):
    """
    Filtra los datos del ciclista con un dorsal específico.
    
    Args:
        df (pd.DataFrame): DataFrame original.
        dorsal (int): Dorsal del ciclista a buscar.
    
    Returns:
        pd.DataFrame: Fila correspondiente al ciclista con el dorsal dado.
    """
    return df[df['dorsal'] == dorsal]

def ejecutar_ejercicio2(data):
    """
    Ejecuta las operaciones del Ejercicio 2: Anonimización y limpieza del dataset.
    
    Args:
        data (pd.DataFrame): DataFrame original.
    
    Returns:
        pd.DataFrame: DataFrame limpio.
    """
    print("EJERCICIO 2: Anonimización y limpieza del dataset")

    # Anonimizar nombres
    datos_anonimizados = name_surname(data)
    print("\nPrimeros 5 registros tras anonimización:")
    print(datos_anonimizados.head())

    # Eliminar no participantes
    datos_limpios = eliminar_no_participantes(datos_anonimizados)
    print(f"\nNúmero de ciclistas tras limpieza: {len(datos_limpios)}")
    print("\nPrimeros 5 registros tras limpieza:")
    print(datos_limpios.head())

    # Recuperar datos del ciclista con dorsal=1000
    ciclista_1000 = filtrar_por_dorsal(datos_limpios, 1000)
    print("\nDatos del ciclista con dorsal=1000:")
    print(ciclista_1000)

    return datos_limpios
