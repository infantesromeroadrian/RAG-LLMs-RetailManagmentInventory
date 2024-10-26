# src/features/cargador_datos_csv.py
import pandas as pd
import time
import logging
from utils.decoradores import time_decorator

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Definir la clase para cargar datos CSV
class CargadorDatosCSV:
    def __init__(self, ruta_archivo):
        """
        Inicializa la clase con la ruta del archivo CSV.
        :param ruta_archivo: Ruta al archivo CSV que contiene los datos de inventario.
        """
        self.ruta_archivo = ruta_archivo
        self.df = None

    @time_decorator
    def cargar_datos(self):
        """
        Carga los datos desde el archivo CSV especificado y los almacena en un DataFrame.
        """
        try:
            start_time = time.time()
            logging.info(f"Cargando datos desde {self.ruta_archivo}...")
            self.df = pd.read_csv(self.ruta_archivo)
            # Añadir una columna de 'Stock' si no existe en el CSV
            if 'Stock' not in self.df.columns:
                self.df['Stock'] = 0  # Inicializar todos los productos con stock 0
            end_time = time.time()
            logging.info(f"Datos cargados exitosamente en {end_time - start_time:.2f} segundos.")
            # Mostrar las columnas cargadas
            logging.info(f"Columnas del DataFrame: {self.df.columns.tolist()}")
        except FileNotFoundError:
            logging.error(f"Error: El archivo en la ruta '{self.ruta_archivo}' no fue encontrado.")
        except pd.errors.EmptyDataError:
            logging.error("Error: El archivo CSV está vacío.")
        except Exception as e:
            logging.error(f"Error inesperado: {e}")