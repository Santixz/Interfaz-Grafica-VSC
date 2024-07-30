from flask import Flask, render_template, request, flash, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'host':'localhost',
    'user':'admin',
    'password':'admin2024',
    'database':'ga_programmers'
}

def procesar_listas(curso, jornada):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute ('INSERT INTO tblistas (curso, jornada) VALUES (%s, %s)',(curso, jornada))
    conn.commit()

@app.route('/')
def procesar_listas():
    return render_template ('listasformulario.html')

@app.route('/insertar_listas', methods = ['POST'])
def insertar_listas():
    curso = request.form['curso']
    jornada = request.form['jornada']

    if not curso or not jornada:
        flash ('Todos los campos son obligatorios')
        return redirect (url_for('listasformulario.html'))
    procesar_listas(curso, jornada)
    return redirect (url_for('imagenesdelistas.html'))

if __name__ == '__main__':
    app.run(debug=True)