# src/utils/decoradores.py
import time
import logging

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Tiempo de ejecución de '{func.__name__}': {end_time - start_time:.2f} segundos")
        return result
    return wrapper

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Ejecutando función: {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Función {func.__name__} completada.")
        return result
    return wrapper