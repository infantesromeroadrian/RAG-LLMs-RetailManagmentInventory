# src/features/gestor_stock.py
import logging
from utils.decoradores import time_decorator, log_decorator

class GestorStock:
    def __init__(self, df):
        """
        Inicializa la clase con el DataFrame del inventario.
        :param df: DataFrame que contiene los datos del inventario.
        """
        self.df = df
        logging.info("Gestor de stock inicializado correctamente.")

    @time_decorator
    @log_decorator
    def actualizar_stock(self, producto_id, cantidad):
        """
        Actualiza el stock de un producto.
        :param producto_id: ID del producto a actualizar.
        :param cantidad: Nueva cantidad a asignar.
        """
        # Verificar que la columna exista y el producto también
        id_col = 'Unique Entry ID'  # Nombre de la columna de ID
        cantidad_col = 'Stock'  # Nombre que asignamos a la columna de cantidad de stock

        if id_col in self.df.columns:
            if producto_id in self.df[id_col].values:
                self.df.loc[self.df[id_col] == producto_id, cantidad_col] = cantidad
                logging.info(f"Stock actualizado para el producto con ID {producto_id}. Nueva cantidad: {cantidad}")
            else:
                logging.warning(f"Producto con ID {producto_id} no encontrado.")
        else:
            logging.error(f"No se encontró la columna '{id_col}' en el DataFrame.")

    @time_decorator
    @log_decorator
    def verificar_stock(self, producto_id):
        """
        Verifica la cantidad de stock de un producto por su ID.
        :param producto_id: ID del producto a verificar.
        :return: Cantidad de stock del producto o None si no se encuentra.
        """
        id_col = 'Unique Entry ID'  # Nombre de la columna de ID
        cantidad_col = 'Stock'  # Nombre de la columna de cantidad de stock

        if id_col in self.df.columns:
            if producto_id in self.df[id_col].values:
                cantidad = self.df.loc[self.df[id_col] == producto_id, cantidad_col].values[0]
                logging.info(f"Consulta de stock realizada para el producto con ID {producto_id}. Resultado: {cantidad} unidades.")
                return cantidad
            else:
                logging.warning(f"Producto con ID {producto_id} no encontrado.")
                return None
        else:
            logging.error(f"No se encontró la columna '{id_col}' en el DataFrame.")
            return None

    @time_decorator
    @log_decorator
    def obtener_dataframe(self):
        """
        Retorna el DataFrame actualizado.
        :return: DataFrame actualizado.
        """
        logging.info("DataFrame del inventario retornado correctamente.")
        return self.df
