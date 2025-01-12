"""
Archivo principal para ejecutar los ejercicios de la PEC4.
"""

import argparse
import os
from ejercicio1 import ejecutar_ejercicio1
from ejercicio2 import ejecutar_ejercicio2
from ejercicio3 import procesar_tiempos
from ejercicio4 import procesar_clubs
from ejercicio5 import analizar_ucsc

def main():
    """
    Función principal para ejecutar los ejercicios de la PEC4.
    """
    # Configuración de argumentos
    parser = argparse.ArgumentParser(description="Ejecutar ejercicios de la PEC4")
    parser.add_argument(
        "--ejercicio",
        type=int,
        choices=range(1, 6),
        help="Número del ejercicio a ejecutar (1-5). Por defecto, ejecuta todos.",
    )

    # Analizar argumentos
    args = parser.parse_args()

    # Ruta multiplataforma al archivo CSV
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(current_dir, "data", "dataset.csv")

    # Control de ejecución de ejercicios
    data = None
    datos_limpios = None
    agrupamiento = None
    clubs_simplificado = None

    # Ejecutar ejercicios en orden si se especifica uno específico
    if args.ejercicio is None or args.ejercicio >= 1:
        print("EJERCICIO 1: Importación del dataset y EDA")
        data = ejecutar_ejercicio1(ruta_csv)
        if data is None:
            print("Error: No se pudo cargar el dataset.")
            return

    if args.ejercicio is None or args.ejercicio >= 2:
        print("EJERCICIO 2: Anonimización y limpieza del dataset")
        datos_limpios = ejecutar_ejercicio2(data)

    if args.ejercicio is None or args.ejercicio >= 3:
        print("EJERCICIO 3: Agrupamiento de los tiempos y generación de histograma")
        agrupamiento = procesar_tiempos(datos_limpios)

    if args.ejercicio is None or args.ejercicio >= 4:
        print("EJERCICIO 4: Limpieza y análisis de clubs ciclistas")
        clubs_simplificado = procesar_clubs(datos_limpios)

    if args.ejercicio is None or args.ejercicio >= 5:
        print("EJERCICIO 5: Análisis de la UCSC (Unió Ciclista Sant Cugat)")
        analizar_ucsc(clubs_simplificado)


if __name__ == "__main__":
    main()
