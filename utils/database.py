# utils/database.py
import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables de entorno desde .env

# Configuración de conexión
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")
driver = os.getenv("SQL_DRIVER")

def get_connection():
    try:
        connection = pyodbc.connect(
            f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        )
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
