from database import get_connection

class Usuario:

    @staticmethod
    def crear(nombre, email, rol):
        conn = get_connection()
        conn.execute(
            'INSERT INTO usuarios (nombre, email, rol) VALUES (?, ?, ?)',
            (nombre, email, rol)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def obtener_todos():
        conn = get_connection()
        usuarios = conn.execute('SELECT * FROM usuarios').fetchall()
        conn.close()
        return usuarios