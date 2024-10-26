# src/interface/app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


# Añadir el directorio src al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import streamlit as st
from features.cargador_datos_csv import CargadorDatosCSV
from features.gestor_stock import GestorStock
from model.sistema_rag import SistemaRAG
from utils.decoradores import time_decorator, log_decorator
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Clase para la interfaz de usuario del sistema de control de stock usando Streamlit
class InterfazUsuario:
    def __init__(self, gestor_stock, sistema_rag):
        self.gestor_stock = gestor_stock
        self.sistema_rag = sistema_rag
        self.titulo_interfaz()
        self.consultar_stock_section()
        self.actualizar_stock_section()
        self.consulta_llm_section()

    def titulo_interfaz(self):
        st.title("Sistema de Control de Stock")

    @time_decorator
    @log_decorator
    def consultar_stock_section(self):
        st.header("Consultar Stock")
        producto_id = st.text_input("ID del Producto:", key="consultar_id")
        if st.button("Consultar Stock"):
            if producto_id:
                cantidad = self.gestor_stock.verificar_stock(producto_id)
                if cantidad is not None:
                    st.success(f"El producto con ID {producto_id} tiene {cantidad} unidades en stock.")
                else:
                    st.warning(f"No se encontró el producto con ID {producto_id}.")
            else:
                st.warning("Por favor, ingrese un ID de producto válido.")

    @time_decorator
    @log_decorator
    def actualizar_stock_section(self):
        st.header("Actualizar Stock")
        producto_id = st.text_input("ID del Producto a Actualizar:", key="actualizar_id")
        cantidad_str = st.text_input("Cantidad de Stock:", key="cantidad_stock")
        if st.button("Actualizar Stock"):
            if producto_id and cantidad_str:
                try:
                    cantidad = int(cantidad_str)
                    self.gestor_stock.actualizar_stock(producto_id, cantidad)
                    st.success(f"El stock del producto con ID {producto_id} ha sido actualizado a {cantidad} unidades.")
                except ValueError:
                    st.warning("Por favor, ingrese un valor numérico para la cantidad de stock.")
            else:
                st.warning("Por favor, complete ambos campos: ID del producto y cantidad.")

    @time_decorator
    @log_decorator
    def consulta_llm_section(self):
        st.header("Consulta con LLM sobre el inventario")
        consulta = st.text_area("Escriba su consulta sobre el inventario:", key="consulta_llm")
        if st.button("Realizar Consulta"):
            if consulta:
                respuesta = self.sistema_rag.realizar_consulta(consulta)
                if respuesta:
                    st.success(f"Respuesta del LLM: {respuesta}")
                else:
                    st.warning("No se obtuvo una respuesta. Intente hacer otra consulta.")
            else:
                st.warning("Por favor, ingrese una consulta.")

# Crear la instancia del cargador de datos CSV
ruta_csv = "data/raw_data/accessories.csv"
cargador = CargadorDatosCSV(ruta_csv)
cargador.cargar_datos()

# Inicializar el gestor del stock con los datos cargados
gestor_stock = GestorStock(cargador.df)

# Inicializar el sistema RAG para consultas al LLM
sistema_rag = SistemaRAG(ruta_csv, os.getenv("OPENAI_API_KEY"))

# Ejecutar la interfaz en Streamlit
if __name__ == "__main__":
    interfaz = InterfazUsuario(gestor_stock, sistema_rag)
