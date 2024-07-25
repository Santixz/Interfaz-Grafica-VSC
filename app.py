from flask import Flask, render_template, request, redirect, seccion, url_for
import mysql.connector
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'
app.config['SESSION TYPE'] = 'filesystem'
Session(app)

db = mysqlconnector(
    host="localhost",
    user="admin"
    password="admin2024"
    database="ga_programmers"
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM tbusuarios")
    datos = cursor.fetchall()
    return render_template('index.html', tbusuarios=tbusuarios)

@app.route('/login')