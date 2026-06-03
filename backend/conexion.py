import os
import pymysql

def obtener_conexion():
    # Si está en Render, usará los datos de la nube; si estás en tu PC, usará los valores por defecto locales
    return pymysql.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', 'AVNS_hxO5F46HlM-9bcUPoY4'),
        database=os.environ.get('DB_NAME', 'sistema_sri'),
        port=int(os.environ.get('DB_PORT', 3306)),
        ssl={'ssl': {}} # ⚠️ ¡IMPORTANTE! Aiven exige conexión segura SSL como muestra tu imagen
    )