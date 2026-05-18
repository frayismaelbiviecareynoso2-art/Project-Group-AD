from flask import Flask, render_template, request, redirect, url_for
from models import Usuario
from database import crear_tabla

app = Flask(__name__)

# Crear tabla al iniciar
crear_tabla()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/crear', methods=['POST'])
def crear_usuario():
    nombre = request.form['nombre']
    email = request.form['email']
    rol = request.form['rol']

    # Validación simple
    if not nombre or not email:
        return "Error: Datos incompletos"

    Usuario.crear(nombre, email, rol)
    return redirect(url_for('ver_usuarios'))

@app.route('/usuarios')
def ver_usuarios():
    usuarios = Usuario.obtener_todos()
    return render_template('usuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)