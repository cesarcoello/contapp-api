from fastapi import FastAPI, HTTPException
from utils.database import get_cursor
from utils.database import get_connection

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}

@app.get("/datos")
def obtener_datos():
    try:
        cursor = get_cursor()
        cursor.execute("SELECT * FROM <tu_tabla>")  # Asegúrate de que esta tabla exista
        rows = cursor.fetchall()
        return {"datos": [dict(zip([column[0] for column in cursor.description], row)) for row in rows]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener datos: {str(e)}")
    
@app.get("/test-connection")
def test_db_connection():
    connection = get_connection()
    if connection:
        connection.close()  # Cerrar la conexión si se estableció
        return {"message": "Conexión exitosa a la base de datos"}
    else:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")