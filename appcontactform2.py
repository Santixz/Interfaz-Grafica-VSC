from flask import Flask, render_template, request, flash, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'host':'localhost',
    'user':'admin',
    'password':'admin2024',
    'database':'ga_programmers'
}

def procesar_contactenos(nombrecompleto, telefono, email, comentario):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tbcontactenos (nombrecompletos, telefono, email, comentario ) VALUES (%s, %s, %s, %s)'(nombrecompleto, telefono, email, comentario))
    conn.commit()

@app.route ('/')
def procesar_contactenos():
    return render_template ('index2.html')

@app.route('/insertar_contactenos', methods = ['POST'])
def insertar_contactenos():
    nombrecompleto = request.form['curso']
    telefono = request.form['jornada']
    email = request.form['email']
    comentario = request.form['comentario']
    if not nombrecompleto or not telefono or not email or not comentario:
        flash ('Todos los campos son obligatorios')
        return redirect (url_for('index2.html'))
    procesar_contactenos(nombrecompleto, telefono, email, comentario)
    return redirect (url_for('exito.html'))

if __name__ == '__main__':
    app.run(debug=True)