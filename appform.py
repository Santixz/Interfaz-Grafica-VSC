from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask (__name__)

db_config = {
    'host':'localhost',
    'user':'admin',
    'password':'admin2024',
    'database':'ga_programmers'
}

def insertar_usuario(nombre, apellido, email, password):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tbusers (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)', (nombre, apellido, email, password))
    conn.commit()
    conn.close()

def obtener_usuario():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, apellido, email FROM tbusers')
    users = cursor.fetchall()
    conn.close
    return users

@app.route('/')
def formulario():
    return render_template ('registrarse.html')

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    nombre = request.form ['nombre']
    apellido = request.form ['apeliido']
    email = request.form ['email']
    contrasena = request.form ['password']
    insertar_usuario(nombre, apellido, email, contrasena)
    return redirect (url_for('exito'))

@app.route ('/users')
def mostrar_usuario():
    users = obtener_usuario()
    return render_template('users.html', usuarios=users)

@app.route ('/eliminar_usuarios/<int:id>', methods = ['POST'])
def eliminar_usuario(id):
    conn = mysql.connector.connect (**db_config)
    cursor = conn.cursor()
    cursor.execute ('DELETE FROM tbusers WHERE id = %s', (id))
    conn.commit
    conn.close
    return redirect (url_for('mostrar_usuario'))

@app.route ('/exito')
def exito():
    return render_template ('exito.html')

if __name__ == '__main__':
    app.run (debug=True)