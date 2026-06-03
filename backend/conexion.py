import os
import pymysql

def obtener_conexion():
    return pymysql.connect(
        host=os.environ.get('DB_HOST'),
        port=int(os.environ.get('DB_PORT', 21545)), # ⬅️ El int() es obligatorio aquí para la nube
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_NAME'),
        ssl={'ssl': {}} # Conexión segura para Aiven
    )