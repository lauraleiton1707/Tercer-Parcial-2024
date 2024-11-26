import time 
import sqlite3 as sql 

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("Base de datos de autoconocimiento creada")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("autoconocimiento")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE respuestas (
    id_respuesta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pregunta INTEGER,
    respuesta_usuario TEXT CHECK(respuesta_usuario IN ('A', 'B')) NOT NULL,
    FOREIGN KEY (id_pregunta) REFERENCES preguntas(id_pregunta)
    ); """)
    print("Tabla Creada")
    
    conn.commit()
    conn.close()

if __name__== "__main__":
    createDB()
    createTable()
