import mysql.connector

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="conexion"
)
cursor = conexion.cursor()

# Crear tabla usuarios
crear_tabla_usuarios = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT PRIMARY KEY,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        correo VARCHAR(100)
    );
"""
cursor.execute(crear_tabla_usuarios)
conexion.commit()

# Crear tabla animales
crear_tabla_animales = """
    CREATE TABLE IF NOT EXISTS animales (
        cod_animales INT PRIMARY KEY,
        nombre_animal VARCHAR(50),
        especie_animal VARCHAR(50),
        color_animal VARCHAR(50)
    );
"""
cursor.execute(crear_tabla_animales)
conexion.commit()

# Insertar datos en la tabla usuarios
insertar_usuarios = """
    INSERT INTO usuarios (id, nombre, apellido, correo) VALUES (%s, %s, %s, %s)
"""
datos_usuarios = (56, "Canelo", "Amarillo", "canelo@gmail.com")
cursor.execute(insertar_usuarios, datos_usuarios)
conexion.commit()

# Insertar datos en la tabla animales
insertar_animales = """
    INSERT INTO animales (cod_animales, nombre_animal, especie_animal, color_animal) VALUES (%s, %s, %s, %s)
"""
datos_animales = (28, "Canelo", "Husky", "Amarillo")
cursor.execute(insertar_animales, datos_animales)
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()

