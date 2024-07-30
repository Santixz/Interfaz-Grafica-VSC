from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from flask_session import Session

app = Flask(__name__)

app.secret_key = 'tu_clave_secreta_aqui'
app.config['SESSION_TYPE'] = 'filesystem'
Session (app)

db = mysql.connector.connect (
    host="localhost",
    user="admin",
    password="admin2024",
    database="ga_programmers"
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM tbusuarios")
    tbusuarios = cursor.fetchall()
    return render_template('index.html', tbusuarios=tbusuarios)


@app.route('/registrarse', methods = ['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        nombre = ['nombre']
        apellido = ['apellido']
        fecha = ['fecha']
        labor = ['labor']
        email = request.form['email']
        contrasena = request.form['contrasena']
        concontrasena = request.form ['concontrasena']
        cursor.execute ("INSERT INTO tbusuarios (nombre, apellido, fecha, labor, email, contrasena, concontrasena) VALUES (%s, %s, %s, %s, %s, %s, %s)",(nombre, apellido, fecha, labor, email, contrasena, concontrasena))
        db.commit()
        return redirect('/')
    return render_template ('index.html')

@app.route('/iniciosesion', methods = ['GET', 'POST'])
def iniciosesion():
    if request.method == 'POST':
        email = request.form['email']
        contrasena = request.form['contrasena']
        cursor.execute("SELECT * FORM tbusuarios WHERE email = %s, contrasena = %s", (email, contrasena))
        user = cursor.fetchone()
        if user:
            session ['email'] = email
            session ['contrasena'] = contrasena
            return redirect (url_for ('index2.html'))
        else:
            return "Credenciales incorrectas. Por favor intentelo de nuevo."
    return render_template('iniciosesion.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('contrasena', None)
    return redirect('index.html')

@app.route('/index2')
def index2():
    if 'email' in session and 'contrasena' in session:
        return render_template('index2.html')
    else: 
        return redirect(url_for('index'))

@app.route('/horarios')
def horarios():
    if 'email' in session and 'contrasena' in session:
        return render_template ('horariosformulario.html')
    else: 
        return redirect(url_for('index'))

@app.route('/listas')
def listas():
    if 'email' in session and 'contrasena' in session:
        return render_template ('listasformulario.html')
    else: 
        return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run (debug=True)