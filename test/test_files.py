import unittest
import pandas as pd
import os

from ejercicio1 import ejecutar_ejercicio1, importar_dataset, analizar_dataset
from ejercicio2 import name_surname, eliminar_no_participantes, filtrar_por_dorsal
from ejercicio3 import minutes_002040, procesar_tiempos
from ejercicio4 import clean_club, procesar_clubs
from ejercicio5 import analizar_ucsc

# Obtener la ruta absoluta del archivo dataset.csv de forma multiplataforma
current_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta absoluta del directorio actual
data_path = os.path.join(current_dir, "..", "data", "dataset.csv")  # Construir ruta al dataset
data_path = os.path.abspath(data_path)  # Convertir a una ruta absoluta

# Clase base para las pruebas que cargue el dataset una vez y proporcione acceso a todas las clases de prueba.
class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Configuración global para cargar el dataset.
        """
        cls.data_path = data_path
        cls.df = importar_dataset(cls.data_path)
        if cls.df is None:
            raise RuntimeError("No se pudo cargar el dataset para las pruebas.")


# Clases individuales heredan de BaseTest
class Test_Ejercicio1(BaseTest):

    def test_importar_dataset_archivo_inexistente(self):
        """
        Verifica que importar_dataset maneja correctamente archivos inexistentes.
        """
        ruta_invalida = "no_existe.csv"
        try:
            data = importar_dataset(ruta_invalida)
        except FileNotFoundError:
            data = None

        self.assertIsNone(data, "importar_dataset debería lanzar un error para un archivo inexistente.")


    def test_ejecutar_ejercicio1(self):
        """
        Verifica que ejecutar_ejercicio1 ejecuta correctamente las operaciones del Ejercicio 1.
        """
        data = ejecutar_ejercicio1(self.data_path)
        self.assertIsInstance(data, pd.DataFrame, "El resultado debe ser un DataFrame.")

    def test_importar_dataset(self):
        """
        Test para verificar que el dataset se importa correctamente.
        """
        self.assertIsInstance(self.df, pd.DataFrame, "El dataset no es un DataFrame.")

    def test_contar_ciclistas(self):
        """
        Test para verificar que el número de ciclistas es positivo y válido.
        """
        total_ciclistas = len(self.df)

        # Verificar que el número de ciclistas es positivo
        self.assertTrue(total_ciclistas > 0, "El número de ciclistas debe ser mayor a 0.")
        self.assertIsInstance(total_ciclistas, int, "El resultado debe ser un número entero.")



class Test_Ejercicio2(BaseTest):

    def test_name_surname(self):
        """
        Verifica que la función name_surname reemplaza correctamente
        los valores de la columna 'biker'.
        """
        # Aplicar la función
        df_anonimizado = name_surname(self.df)

        # Comprobar que los nombres han sido reemplazados
        for original, anon in zip(self.df['biker'], df_anonimizado['biker']):
            self.assertNotEqual(original, anon, f"El nombre '{original}' no fue reemplazado.")


    def test_name_surname_simulado(self):
        """
        Verifica que name_surname reemplaza correctamente los valores de la columna 'biker' en un dataset simulado.
        """
        data_simulado = pd.DataFrame({
            'dorsal': [1, 2],
            'biker': ['John Doe', 'Jane Smith'],
            'time': ['01:00:00', '01:10:00']
        })

        df_anonimizado = name_surname(data_simulado)

        # Verificar que los nombres han sido reemplazados
        for original, anon in zip(data_simulado['biker'], df_anonimizado['biker']):
            self.assertNotEqual(original, anon, f"El nombre '{original}' no fue reemplazado correctamente.")


    def test_eliminar_no_participantes_caso_extremo(self):
        """
        Verifica que eliminar_no_participantes elimina correctamente todos los ciclistas
        cuando todos tienen tiempo '00:00:00'.
        """
        data_simulado = pd.DataFrame({
            'dorsal': [1, 2],
            'biker': ['John Doe', 'Jane Smith'],
            'time': ['00:00:00', '00:00:00']
        })

        resultado = eliminar_no_participantes(data_simulado)
        self.assertEqual(len(resultado), 0, "Debería eliminar todos los ciclistas con tiempo '00:00:00'.")

    def test_eliminar_no_participantes(self):
        """
        Verifica que la función eliminar_no_participantes elimina correctamente
        a los ciclistas que no participaron (time = '00:00:00'), que el número
        de participantes sea mayor a 0 y menor que en el dataset original.
        """
        # Aplicar la función
        df_limpio = eliminar_no_participantes(self.df)

        # Comprobar que el número de filas es mayor que 0
        self.assertGreater(len(df_limpio), 0, "El número de participantes debe ser mayor que cero.")

        # Comprobar que el número de filas es menor que en el dataset original
        self.assertLess(len(df_limpio), len(self.df), "El número de participantes no se redujo.")

    def test_filtrar_por_dorsal(self):
        """
        Verifica que la función filtrar_por_dorsal recupera correctamente
        la fila correspondiente al dorsal especificado y que devuelve
        exactamente una fila si el dorsal es único.
        """
        # Caso 1: Dorsal existente y único
        resultado = filtrar_por_dorsal(self.df, 1000)

        # Verificar que el resultado no está vacío
        self.assertGreater(len(resultado), 0, "El número de filas devueltas debe ser mayor que 0.")

        # Verificar que exactamente una fila sea devuelta
        self.assertEqual(len(resultado), 1, "El número de filas devueltas debe ser igual a 1.")

class Test_Ejercicio3(BaseTest):

    def test_minutes_002040(self):
        """
        Verifica que la función minutes_002040 agrupa correctamente los tiempos.
        """
        # Casos de prueba
        self.assertEqual(minutes_002040('06:19:40'), '06:00', "El tiempo 06:19:40 debería agruparse como 06:00.")
        self.assertEqual(minutes_002040('06:29:40'), '06:20', "El tiempo 06:29:40 debería agruparse como 06:20.")
        self.assertEqual(minutes_002040('06:59:40'), '06:40', "El tiempo 06:59:40 debería agruparse como 06:40.")
        self.assertEqual(minutes_002040('07:10:15'), '07:00', "El tiempo 07:10:15 debería agruparse como 07:00.")

    def test_procesar_tiempos(self):
        """
        Verifica que procesar_tiempos agrega correctamente la columna agrupada
        """
        # Aplicar la función
        grouped_df = procesar_tiempos(self.df)

        # Verificar que la columna 'time_grouped' fue creada correctamente
        self.assertIn('time_grouped', grouped_df.columns, "La columna 'time_grouped' no fue creada en el DataFrame.")

class Test_Ejercicio4(BaseTest):

    def test_clean_club(self):
        """
        Verifica que la función clean_club limpia correctamente los nombres de los clubs.
        """
        # Casos de prueba
        self.assertEqual(clean_club('C.C. Huesca'), 'HUESCA', "No limpió correctamente 'C.C. Huesca'.")
        self.assertEqual(clean_club('C.C. CASTILLO DE MULA'), 'CASTILLO DE MULA', "No limpió correctamente 'Club Ciclista Huesca'.")
        self.assertEqual(clean_club('INDEPENDIENTE'), 'INDEPENDIENTE', "No limpió correctamente 'INDEPENDIENTE'.")
        self.assertEqual(clean_club('Peña Ciclista Zaragoza'), 'ZARAGOZA', "No limpió correctamente 'Peña Ciclista Zaragoza'.")
        self.assertEqual(clean_club('CLUB ciclista Sariñena'), 'SARIÑENA', "No limpió correctamente 'Peña Ciclista Zaragoza'.")

    def test_procesar_clubs(self):
        """
        Verifica que procesar_clubs  agrupa los datos.
        """
        # Aplicar la función
        grouped_df = procesar_clubs(self.df)

        # Verificar que la columna 'club_clean' fue creada
        self.assertIn('club_clean', grouped_df.columns, "La columna 'club_clean' no fue creada en el DataFrame.")


class Test_Ejercicio5(BaseTest):
    @classmethod
    def setUpClass(cls):
        """
        Configuración adicional específica para Ejercicio 5.
        """
        super().setUpClass()
        cls.df = procesar_clubs(cls.df)

    def test_analizar_ucsc(self):
        """
        Verifica que el análisis de la UCSC funciona correctamente cuando hay ciclistas de este club.
        """
        # Usar cls.df en lugar de self.data
        resultados = analizar_ucsc(self.df)

        # Verificar el mejor ciclista de la UCSC
        mejor_ciclista = resultados['mejor_ciclista']
        self.assertEqual(mejor_ciclista['dorsal'], 415, "El mejor ciclista de la UCSC debería tener dorsal 415.")


if __name__ == "__main__":
    # Configurar un cargador de pruebas
    loader = unittest.TestLoader()

    # Crear suites de prueba a partir de las clases
    suite_ej1 = loader.loadTestsFromTestCase(Test_Ejercicio1)
    suite_ej2 = loader.loadTestsFromTestCase(Test_Ejercicio2)
    suite_ej3 = loader.loadTestsFromTestCase(Test_Ejercicio3)
    suite_ej4 = loader.loadTestsFromTestCase(Test_Ejercicio4)
    suite_ej5 = loader.loadTestsFromTestCase(Test_Ejercicio5)

    # Combinar todas las suites en una sola
    all_tests = unittest.TestSuite([suite_ej1, suite_ej2, suite_ej3, suite_ej4, suite_ej5])

    # Ejecutar todas las pruebas con un solo runner
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(all_tests)