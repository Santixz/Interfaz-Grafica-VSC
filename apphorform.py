from flask import Flask, render_template, request, flash, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'host':'localhost',
    'user':'admin',
    'password':'admin2024',
    'database':'ga_programmers'
}

def procesar_curso(curso, jornada):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute ('INSERT INTO tbhorarios (curso, jornada) VALUES (%s, %s)',(curso, jornada))
    conn.commit()

@app.route('/')
def procesar_curso():
    return render_template ('horariosformulario.html')

@app.route('/insertar_curso', methods = ['POST'])
def insertar_curso():
    curso = request.form['curso']
    jornada = request.form['jornada']

    if not curso or not jornada:
        flash ('Todos los campos son obligatorios')
        return redirect (url_for('horariosformulario.html'))
    procesar_curso(curso, jornada)
    return redirect (url_for('imagenesdehorarios.html'))
