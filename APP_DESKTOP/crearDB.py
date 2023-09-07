import sqlite3

# Nombre de la base de datos
db_name = 'db_usuarios.db'

# Conectar a la base de datos (se creará si no existe)
conexion = sqlite3.connect(db_name)
cursor = conexion.cursor()

# Crear la tabla 'Productos' si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        DNI TEXT NOT NULL,
        Nombres TEXT NOT NULL,
        Apellidos TEXT NOT NULL,
        Sexo TEXT NOT NULL,
        Edad INTEGER NOT NULL,
        Correo TEXT NOT NULL,
        Contraseña TEXT NOT NULL,
        Respuesta TEXT NOT NULL
    )
''')

# Guardar los cambios y cerrar la conexión a la base de datos
conexion.commit()
conexion.close()

print(f"Base de datos '{db_name}' creada exitosamente.")