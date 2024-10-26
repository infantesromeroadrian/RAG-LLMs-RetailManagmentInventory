# src/main.py
#%%
from src.model.sistema_rag import SistemaRAG
from features.cargador_datos_csv import CargadorDatosCSV
from features.gestor_stock import GestorStock
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Crear la instancia del cargador de datos CSV
ruta_csv = "../data/raw_data/accessories.csv"
cargador = CargadorDatosCSV(ruta_csv)
cargador.cargar_datos()

#%%
# Crear la instancia del sistema RAG
sistema_rag = SistemaRAG(ruta_archivo=ruta_csv, api_key=openai_api_key)

# Realizar una consulta al sistema RAG
consulta = "What is the price of the black 3D glasses?"
response = sistema_rag.realizar_consulta(consulta)
print(response)

#%%
# Inicializamos el gestor del stock con los datos cargados
gestor_stock = GestorStock(cargador.df)

# Actualizamos el stock de un producto específico
gestor_stock.actualizar_stock(producto_id='FNxEraBTeWRiCvtFu', cantidad=45)

# Verificar la cantidad de stock del producto actualizado
gestor_stock.verificar_stock(producto_id='FNxEraBTeWRiCvtFu')

# Verificar el DataFrame actualizado
df_actualizado = gestor_stock.obtener_dataframe()
print(df_actualizado.head())
