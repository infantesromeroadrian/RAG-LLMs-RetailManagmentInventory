# src/model/sistema_rag.py
# Accedemos a nuestras claves API con dotenv
import os
import time
import logging
from dotenv import load_dotenv
from langchain_openai import OpenAI, ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from src.utils.decoradores import time_decorator
from dotenv import load_dotenv
import os

# environment variables
load_dotenv()

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cargar las variables de entorno
load_dotenv()
# OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")


# Definir la clase para el sistema RAG
class SistemaRAG:
    def __init__(self, ruta_archivo, api_key, chunk_size=1000, chunk_overlap=0):
        """
        Inicializa el sistema RAG con los parámetros proporcionados.
        :param ruta_archivo: Ruta al archivo que contiene los datos de entrada.
        :param api_key: Clave API para acceder a los servicios de OpenAI.
        :param chunk_size: Tamaño de cada chunk al dividir el documento.
        :param chunk_overlap: Solapamiento entre los chunks de texto.
        """
        self.ruta_archivo = ruta_archivo
        self.api_key = api_key
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.vector_db = None
        self.retriever = None
        self.chat_model = ChatOpenAI(model="gpt-4o-mini", api_key=self.api_key)

        # Inicializar la carga de documentos y procesamiento
        self._cargar_y_procesar_documento()

    @time_decorator
    def _cargar_y_procesar_documento(self):
        """
        Carga el documento y lo procesa para dividirlo en chunks y crear la base de datos vectorial.
        """
        start_time = time.time()
        logging.info("Cargando y procesando el documento...")

        # Cargar documento
        loader = TextLoader(self.ruta_archivo)
        loaded_document = loader.load()

        # Dividir el documento en chunks
        text_splitter = CharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        chunks_of_text = text_splitter.split_documents(loaded_document)

        # Crear los embeddings usando OpenAI
        embeddings = OpenAIEmbeddings(api_key=self.api_key)

        # Crear la base de datos vectorial con FAISS
        self.vector_db = FAISS.from_documents(chunks_of_text, embeddings)

        # Crear el retriever para buscar documentos
        self.retriever = self.vector_db.as_retriever(search_kwargs={"k": 5})

        end_time = time.time()
        logging.info(f"Documento cargado y procesado en {end_time - start_time:.2f} segundos")

    @time_decorator
    def realizar_consulta(self, consulta):
        """
        Realiza una consulta al sistema RAG y devuelve la respuesta.
        :param consulta: La consulta a realizar.
        :return: Respuesta generada por el sistema RAG.
        """
        logging.info(f"Realizando consulta: {consulta}")

        # Crear el template de prompt
        prompt_template = """Answer the question based only on the following context:

{context}

Question: {question}
"""
        prompt = ChatPromptTemplate.from_template(prompt_template)

        # Crear una función para formatear los documentos recuperados
        def format_docs(docs):
            return "\n\n".join([d.page_content for d in docs])

        # Crear la cadena completa para invocar al modelo
        chain = (
                {"context": self.retriever | format_docs, "question": RunnablePassthrough()}
                | prompt
                | self.chat_model
                | StrOutputParser()
        )

        # Realizar la consulta
        response = chain.invoke(consulta)
        logging.info(f"Consulta realizada. Respuesta: {response}")
        return response