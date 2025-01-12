# PEC4

## Autor
**Etel Silva Garcia**

---

## Contenido del Proyecto

El proyecto está compuesto por los siguientes archivos y carpetas:

1. **main.py**: Fichero principal que debe ejecutarse para interactuar con el proyecto.
2. **Archivos por Ejercicio**:
   - **ejercicio1.py**: Incluye las funciones correspondientes al ejercicio 1.
   - **ejercicio2.py**: Incluye las funciones correspondientes al ejercicio 2.
   - **ejercicio3.py**: Incluye las funciones correspondientes al ejercicio 3.
   - **ejercicio4.py**: Incluye las funciones correspondientes al ejercicio 4.
   - **ejercicio5.py**: Incluye las funciones correspondientes al ejercicio 5.
4. **Requirements**: Fichero requirements.txt con las dependencias del proyecto
5. **Carpeta `test`**: Contiene el archivo `test_files.py` para ejecutar las pruebas unitarias y analizar la cobertura de código.
5. **Carpeta `data`**: Contiene el archivo `dataset.csv`, necesario para la correcta ejecución del programa.

---

## Cómo Usar el Programa

### Requisitos
- **IDE Utilizado:** PyCharm
- **Sistema Operativo:** Windows
- **Versión de Python:** Python 3.12.6

### Ejecución de `main.py`

El archivo `main.py` permite:
1. **Ejecutar todas las funciones de la PEC4 por defecto**:
   - Esto incluye la ejecución de todos los ejercicios del 1 al 5 en orden, mostrando los resultados por pantalla.
   - **Comando:**
     ```bash
     python main.py
     ```

2. **Ejecutar un ejercicio específico**:
   - Puedes indicar el número de ejercicio que deseas ejecutar (del 1 al 5) usando el argumento `--ejercicio`.
   - Ten en cuenta que para ejecutar un ejercicio, primero se ejecutarán todos los ejercicios anteriores necesarios para garantizar el correcto funcionamiento.
   - **Ejemplo:**
     ```bash
     python main.py --ejercicio 3
     ```

---

## Ejecución de Tests

### Ejecución de Pruebas Unitarias
El archivo `test_files.py` contiene todas las pruebas unitarias necesarias para verificar que las funciones del proyecto funcionan correctamente.
   - Para ejecutar las pruebas unitarias, utiliza el siguiente comando desde el directorio raíz del proyecto:
     ```bash
     python -m unittest discover -s test -p "test_files.py"
     ```

---
### Ejecución de Prueba de cobertura
   - Para ejecutar las pruebas de cobertura, utiliza el siguiente comando desde el directorio raíz del proyecto:
     ```bash
     coverage run -m unittest discover -s test -p "test_files.py"
     ```

   - Para generar el reporte de cobertura en consola, después de ejecutar coverage run,utiliza el siguiente comando desde el directorio raíz del proyecto:
     ```bash
     coverage report -m
     ```
---

## Pruebas de Estilo con pylint
- Utiliza el siguiente comando desde el directorio raíz del proyecto:
     ```bash
     pylint *.py
     ```
---

